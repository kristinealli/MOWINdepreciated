from typing import List, Dict

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class UserCardProgress(models.Model):
    """
    Tracks a user's progress and interaction with a specific card.
    Stores the user's box level for the card, last review date, next review date, and whether the round was completed.
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    box_level = models.IntegerField(default=1)
    last_reviewed = models.DateTimeField(default=timezone.now)
    next_review_date = models.DateTimeField(default=timezone.now)
    review_log: List[Dict[str, str]] = []
    card_mastered = models.BooleanField(default=False) 
    card_due_for_review = models.BooleanField(default=False) 
    
#Return True if the card is due for review, False otherwise.
    def due_for_review(self) -> bool:
        return timezone.now() >= self.next_review_date
  
    class Meta:
        unique_together = ['user', 'card']
        indexes = [
            models.Index(fields=['user', 'next_review_date']),
            models.Index(fields=['user', 'box_level']),
        ]
        ordering = ['next_review_date']



