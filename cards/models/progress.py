from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .card import Card

class UserCardProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    box_level = models.IntegerField(default=1)
    last_reviewed = models.DateTimeField(default=timezone.now)
    next_review_date = models.DateTimeField(default=timezone.now)
    round_completed = models.BooleanField(default=False)
    last_review_result = models.BooleanField(default=False) 