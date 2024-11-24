from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet, Manager
from django.utils import timezone

from cards.models.progress import UserCardProgress

User = get_user_model()

class Deck(models.Model):
    """
    Represents a collection of flashcards organized as a deck.

    Attributes:
        name (str): The name of the deck
        description (str): Optional description of the deck 
        owner (User): The user who created the deck (and is able to edit it)
        cards (ManyToManyField): Collection of cards in this deck
        date_created (datetime): When the deck was created
        is_public (bool): Whether the deck is publicly accessible
        updated_at (datetime): When the deck was last modified
    """
    objects: Manager = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_progress(self, user) -> float:
        """Returns percentage of cards marked as mastered - is displayed in the dashboard"""
        cards_queryset: QuerySet = UserCardProgress.objects.filter(user=user, card__deck=self)
        total_cards: int = cards_queryset.count()
        mastered_cards: int = cards_queryset.filter(card_mastered =True).count()
        return (mastered_cards / total_cards) * 100 if total_cards > 0 else 0

    def get_due_cards(self, user):
        return UserCardProgress.objects.filter(
            user=user,
            card__deck=self,
            next_review_date__lte=timezone.now()
        )

    class Meta:
        ordering = ['-date_created']
        indexes = []