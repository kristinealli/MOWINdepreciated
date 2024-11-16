from typing import cast

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone

User = get_user_model()


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class UserDeck(models.Model):
    """
    Tracks a user's progress and interaction with a specific deck (student's notebook)

    Attributes:
        user (User): The user studying the deck
        deck (Deck): The deck being studied
        last_reviewed (datetime): When the deck was last reviewed (by the user)
        progress (float): Completion percentage
        cards_mastered (int): Number of cards marked as known
        review_streak (int): Consecutive days of review
    """
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey('cards.Deck', on_delete=models.CASCADE) # Lazy import to avoid circular dependency  
    last_reviewed = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False) #TO DO: Add to UI
    progress = models.FloatField(default=0.0)  # Store progress as percentage
    cards_mastered = models.PositiveIntegerField(default=0)
    review_streak = models.PositiveIntegerField(default=0)  # Days in a row
    next_review_date = models.DateTimeField(null=True, blank=True)
    custom_notes = models.TextField(blank=True)

    # Statistics
    total_reviews = models.PositiveIntegerField(default=0)
    correct_answers = models.PositiveIntegerField(default=0)
    incorrect_answers = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        """Return string representation of UserDeck"""
        return f"{self.user.get_username()} - {self.deck.name}"
    
    def start_study_session(self) -> QuerySet:
        """Get cards due for review in this deck"""
        return self.deck.get_due_cards().filter(
            usercardprogress__user=self.user
        )

    def process_review(self, card: 'Card', quality: int) -> None:
        """
        Process a card review in a study session
        Args:
            card: The card being reviewed
            quality: Review quality (1-4)
        """
        progress, _ = UserCardProgress.objects.get_or_create(
            user=self.user,
            card=card
        )
        progress.review(quality)
        
        # Update deck statistics
        self.total_reviews += 1
        self.last_reviewed = timezone.now()
        if quality >= 3:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.update_streak()
        self.save()
    
    def update_progress(self) -> None:
        """Update progress based on cards mastered"""
        total_cards: int = cast(QuerySet, self.deck.cards.all()).count()
        if total_cards > 0:
            self.progress = (self.cards_mastered / total_cards) * 100
            self.save()

    def update_streak(self):
        """Update review streak based on consecutive days"""
        today = timezone.now()
        if self.last_reviewed:
            days_diff = (today - self.last_reviewed).days
            if days_diff <= 1:
                self.review_streak += 1
            else:
                self.review_streak = 0
        self.last_reviewed = today
        self.save()

    def get_accuracy(self) -> float:
        """Calculate review accuracy percentage"""
        total: int = self.total_reviews
        return (self.correct_answers / total * 100) if total > 0 else 0

    def record_review_result(self, was_correct: bool) -> None:
        """
        Record the result of a card review
        
        Args:
            was_correct: Whether the user answered correctly
        """
        self.total_reviews += 1
        if was_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.save()

    class Meta:
        unique_together = ['user', 'deck']
        ordering = ['-last_reviewed']
        indexes = [
            models.Index(fields=['user', 'last_reviewed']),
            models.Index(fields=['user', 'is_favorite']),
        ]

class UserCardProgress(models.Model):
    """
    Tracks user progress on individual cards, including box level and review history.
    """
    id: int = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        """Return string representation of UserCardProgress."""
        try:
            card = self.card  # Django will handle lazy loading
            return str(f"{self.user.username} - {card.anishinaabemowin}")
        except ObjectDoesNotExist:
            return str(f"UserCardProgress {self.id} - Card or User not found")

    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    box_level = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])
    last_reviewed = models.DateTimeField(auto_now_add=True)
    next_review_date = models.DateTimeField(null=True, blank=True)
    round_completed = models.BooleanField(default=False)
    known = models.BooleanField(default=False)
    last_review_result = models.BooleanField(null=True)  # Track last attempt
    review_history = models.JSONField(default=list)  # Store detailed history

    # Statistics
    total_attempts = models.PositiveIntegerField(default=0)
    correct_attempts = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=0)  # Consecutive correct

    def review(self, quality: int) -> None:
        """
        Review a card using a quality rating system
        Args:
            quality: 1 (fail), 2 (hard), 3 (good), 4 (easy)
        """
        # Leitner system intervals (in days)
        intervals = {
            1: 0,      # Repeat today
            2: 1,      # Tomorrow
            3: 3,      # 3 days
            4: 7,      # 1 week
            5: 14      # 2 weeks
        }

        # Update box level based on quality
        if quality >= 3:  # Good/Easy
            if self.box_level < 5:
                self.box_level += 1
        else:  # Fail/Hard
            self.box_level = max(1, self.box_level - 1)

        # Update statistics
        self.total_attempts += 1
        success = quality >= 3
        if success:
            self.correct_attempts += 1
            self.streak += 1
        else:
            self.streak = 0

        # Update review dates
        self.last_reviewed = timezone.now()
        self.next_review_date = self.last_reviewed + timezone.timedelta(
            days=intervals[self.box_level]
        )
        self.last_review_result = success
        
        # Add to review history
        self.review_history.append({
            'date': self.last_reviewed.isoformat(),
            'quality': quality,
            'box_level': self.box_level
        })
        
        self.save()

    def get_accuracy(self) -> float:
        """Calculate success rate"""
        if self.total_attempts == 0:
            return 0
        return (self.correct_attempts / self.total_attempts) * 100

    def calculate_next_review(self) -> None:
        """Calculate next review date based on box level"""
        intervals: dict[int, timezone.timedelta] = {
            1: timezone.timedelta(hours=4),
            2: timezone.timedelta(days=1),
            3: timezone.timedelta(days=3),
            4: timezone.timedelta(days=7),
            5: timezone.timedelta(days=14)
        }
        self.next_review_date = timezone.now() + intervals.get(self.box_level)
        self.save()

    def move(self, solved):
        """Move card to next box if solved, or back to first box if failed"""
        new_box = self.box_level + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box_level = new_box
            self.save()

        return self

    class Meta:
        unique_together = ['user', 'card']
        indexes = [
            models.Index(fields=['user', 'next_review_date']),
            models.Index(fields=['user', 'box_level']),
        ]
        ordering = ['next_review_date']
       
export_models = [UserDeck, UserCardProgress]
