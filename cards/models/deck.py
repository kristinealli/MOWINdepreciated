from typing import cast

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet, Manager
from django.contrib.auth.models import User as DjangoUser
from django.utils import timezone

User = get_user_model()


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Deck(models.Model):
    """
    Represents a collection of flashcards organized as a deck.

    Attributes:
        name (str): The name of the deck
        owner (User): The user who created the deck
        cards (ManyToManyField): Collection of cards in this deck
        description (str): Optional description of the deck
        created_at (datetime): When the deck was created
        updated_at (datetime): When the deck was last modified
        is_public (bool): Whether the deck is publicly accessible
    """
    objects: Manager = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,  # Temporarily allow null
        blank=True  # Temporarily allow blank
    )
    date_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='decks', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_progress(self) -> float:
        """Returns percentage of cards marked as known."""
        cards_queryset: QuerySet = self.cards.all()
        total_cards: int = cards_queryset.count()
        known_cards: int = cards_queryset.filter(known=True).count()
        return (known_cards / total_cards) * 100 if total_cards > 0 else 0

    def get_due_cards(self) -> QuerySet:
        """Returns cards due for review based on user progress"""
        return self.cards.filter(
            usercardprogress__next_review_date__lte=timezone.now()
        ).distinct()

    def reset_progress(self) -> None:
        """Resets all cards to box 1"""
        cards_queryset: QuerySet = cast(QuerySet, self.cards.all()) # type: ignore
        cards_queryset.update(box=1)
    
    def get_user_permissions(self, user: DjangoUser) -> str:
        """
        Get the permission level for a specific user.
        DjangoUser is the built-in User model.
        
        Returns:
            str: Permission level ('VIEW', 'EDIT', 'ADMIN', or None)
        """
        if user == self.owner:
            return 'ADMIN'
        try:
            share = DeckShare.objects.get(
                deck=self,
                shared_with=user,
                active=True
            )
            return share.permissions
        except DeckShare.DoesNotExist:
            return None if not self.is_public else 'VIEW'

    class Meta:
        ordering = ['-date_created']
        indexes = []


class DeckShare(models.Model):
    """
    Manages sharing of decks between users with specific permissions.
    
    Attributes:
        deck (Deck): The deck being shared
        shared_by (User): User who shared the deck
        shared_with (User): User who received the share
        permissions (str): Level of access granted
        date_shared (datetime): When the share was created
        can_edit (bool): Whether the recipient can modify cards
    """
    PERMISSION_CHOICES = [
        ('VIEW', 'View Only'),
        ('EDIT', 'Can Edit'),
        ('ADMIN', 'Admin Access')
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='shared_decks'
    )
    shared_with = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_shares'
    )
    permissions = models.CharField(
        max_length=10, 
        choices=PERMISSION_CHOICES, 
        default='VIEW'
    )
    date_shared = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['deck', 'shared_with']
        indexes = [
            models.Index(fields=['shared_with', 'active']),
            models.Index(fields=['deck', 'active']),
        ]

export_models = [Deck, DeckShare]
