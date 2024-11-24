# Django imports 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import  redirect


# Local imports
from cards.models import Deck, UserCardProgress

# Curriculum Views
@login_required
def curriculum_view(request):
    chosen_decks = request.user.profile.chosen_decks.all()
    all_decks = Deck.objects.all()
    available_decks = all_decks.exclude(id__in=chosen_decks.values_list('id', flat=True))

    context = {
        'decks': chosen_decks,
        'available_decks': available_decks,
    }
    return render(request, 'cards/user_deck_list.html', context)

@login_required
def add_to_curriculum(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    cards = deck.cards.all()
    if request.method == 'POST':
        # Add deck to user's curriculum
        request.user.profile.chosen_decks.add(deck)
        
        # Create initial progress entries for all cards in this deck
        now = timezone.now()
        
        # Check existing progress records to avoid duplicates
        existing_progress = UserCardProgress.objects.filter(user=request.user, card__in=cards)
        existing_card_ids = existing_progress.values_list('card_id', flat=True)
        
        # Bulk create progress entries for each card not already in progress
        new_progress = [
            UserCardProgress(
                user=request.user,
                card=card,
                box_level=1,  # All new cards start in box 1
                next_review_date=now,  # Due immediately
            ) for card in cards if card.id not in existing_card_ids
        ]
        
        UserCardProgress.objects.bulk_create(new_progress)
        
        print(f"Added {len(new_progress)} new progress records for deck '{deck.name}'")
        
        messages.success(request, f'"{deck.name}" has been added to your curriculum.')
        
    return redirect('user_deck_list')

@login_required
def remove_from_curriculum(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id )
    if request.method == 'POST':
        request.user.profile.chosen_decks.remove(deck)
        UserCardProgress.objects.filter(user=request.user, card__in=deck.cards.all()).delete()
        
        messages.success(request, f'"{deck.name}" has been removed from your curriculum and progress has been deleted.')
        
            # Clear dashboard cache to ensure updated counts are shown
        cache_key = f'dashboard_data_{request.user.id}'
        cache.delete(cache_key)
        
    return redirect('user_deck_list')
    