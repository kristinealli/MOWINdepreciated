from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=100, null=True, blank=True)
    chosen_decks = models.ManyToManyField('Deck', related_name='profiles', blank=True) #Different than userdecks -- 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def decks_in_curriculum(self):
        return self.chosen_decks.count()

    def __str__(self):
        return f"{self.user.username}'s profile"

# Signal to automatically create profile and user deck when user is created
@receiver(post_save, sender=User)
def create_user_profile_and_deck(instance, created, **kwargs):
    """
    Signal handler that creates a Profile and a UserDeck when a User is created

    Args:
        sender: The User model class
        instance: The actual User instance that was saved
        created: Boolean indicating if this is a new User
    """
    if created:  # only create profile and user deck for new users
        from cards.models import UserDeck 
        profile = Profile.objects.create(user=instance)
        UserDeck.objects.create(profile=profile)

@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    """
    Signal handler that saves a Profile when a User is saved
    """
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        from cards.models import UserDeck 
        profile = Profile.objects.create(user=instance)
        UserDeck.objects.create(profile=profile)
