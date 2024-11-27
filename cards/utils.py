from django.utils import timezone
from cards.models import UserCardProgress

def create_progress_entries(user, cards):
    """
    Ensure progress entries exist for all cards.
    """
    existing_cards = UserCardProgress.objects.filter(user=user, card__in=cards).values_list('card_id', flat=True)
    new_progress = [
        UserCardProgress(user=user, card=card, next_review_date=timezone.now())
        for card in cards if card.id not in existing_cards
    ]
    UserCardProgress.objects.bulk_create(new_progress)
