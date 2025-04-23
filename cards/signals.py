from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from cards.models import Profile, UserCardProgress

@receiver(m2m_changed, sender=Profile.chosen_decks.through)
def sync_user_deck(sender, instance, action, **kwargs):
    """
    Synchronize UserDeck cards whenever chosen_decks is modified.
    """
    if action in ['post_add', 'post_remove', 'post_clear']:
        # Update the cards in UserDeck
        instance.user_deck.update_cards()
        
        # Ensure progress entries are created for all cards in UserDeck
        from cards.utils import create_progress_entries  
        create_progress_entries(instance.user, instance.user_deck.cards.all())
