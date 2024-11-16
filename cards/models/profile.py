from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=100, null=True, blank=True)
    chosen_decks = models.ManyToManyField('Deck', related_name='profiles', blank=True)
    study_streak = models.PositiveIntegerField(default=0)
    last_study_date = models.DateField(null=True, blank=True)
    total_cards_studied = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def decks_in_curriculum(self):
        return self.chosen_decks.count()

    def __str__(self):
        return f"{self.user.username}'s profile"

    def update_study_streak(self) -> None:
        """Update study streak based on consecutive days of study"""
        today = timezone.now().date()
        if self.last_study_date:
            days_diff = (today - self.last_study_date).days
            if days_diff <= 1:  # If studied yesterday or today
                self.study_streak += 1
            else:  # Streak broken
                self.study_streak = 1  # Reset to 1 since they're studying today
        else:
            self.study_streak = 1
        
        self.last_study_date = today
        self.save()

    def record_study_session(self, cards_studied: int) -> None:
        """
        Record a study session, updating last_study_date and total_cards_studied
        
        Args:
            cards_studied: Number of cards reviewed in this session
        """
        self.last_study_date = timezone.now().date()
        self.total_cards_studied += cards_studied
        self.update_study_streak()  # Update streak while we're at it
        self.save()

# Signal to automatically create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler that creates a Profile when a User is created

    Args:
        sender: The User model class
        instance: The actual User instance that was saved
        created: Boolean indicating if this is a new User
        **kwargs: Additional arguments passed by the signal
    """
    if created:  # only create profile for new users
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **_kwargs):
    """
    Signal handler that saves a Profile when a User is saved
    """
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)

export_models = [Profile]
