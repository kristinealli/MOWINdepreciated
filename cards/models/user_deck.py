from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDeck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_decks')
    deck = models.ForeignKey('cards.Deck', on_delete=models.CASCADE, related_name='user_decks')
    is_owner = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'deck']

    def __str__(self):
        return f"{self.user.username} - {self.deck.name}" 