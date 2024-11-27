import django.db.models as models
from django.utils import timezone

from cards.models import Card, UserCardProgress, Profile

class UserDeck(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user_deck')
    cards = models.ManyToManyField(Card)

    def __str__(self) -> str:
        return f"{self.profile.user.username}'s Deck"
        
    def update_cards(self):
        """
        Synchronize UserDeck cards with the chosen_decks.
        """
        all_cards = Card.objects.filter(deck__in=self.profile.chosen_decks.all())
        self.cards.set(all_cards)
