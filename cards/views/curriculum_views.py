import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.cache import cache

# Local imports
from cards.models import Deck, UserCardProgress
from cards.utils import create_progress_entries
logger = logging.getLogger(__name__)


# Curriculum Views
@login_required
def curriculum_view(request):

    user = request.user
    deck_list = Deck.objects.all() 
    chosen_decks = user.profile.chosen_decks.all()
    available_decks = deck_list.exclude(id__in=chosen_decks.values_list('id', flat=True))
 
    context = {
        'chosen_decks': chosen_decks,
        'available_decks': available_decks,
    }
    return render(request, 'cards/deck_list.html', context)
    
    
@login_required
def curriculum_view_modify(request):

    user = request.user
    deck_list = Deck.objects.all() 
    chosen_decks = user.profile.chosen_decks.all()
    available_decks = deck_list.exclude(id__in=chosen_decks.values_list('id', flat=True))
 
    context = {
        'decks': chosen_decks,
        'available_decks': available_decks,
    }
    return render(request, 'cards/user_deck_list.html', context)


@login_required
def add_to_curriculum(request, deck_id):
    """
    Add a deck to the user's curriculum and update UserDeck and UserCardProgress.
    """
    deck = get_object_or_404(Deck, pk=deck_id)

    if request.method == 'POST':
        # Add the deck to chosen decks
        request.user.profile.chosen_decks.add(deck)

        # Synchronize UserDeck cards
        request.user.profile.user_deck.update_cards()

        # Create progress entries for new cards
        create_progress_entries(request.user, request.user.profile.user_deck.cards.all())

        messages.success(request, f'"{deck.name}" has been added to your curriculum.')

    return redirect('user_deck_list')


@login_required
def remove_from_curriculum(request, deck_id):
    """
    Remove a deck from the user's curriculum and clean up UserDeck and UserCardProgress.
    """
    deck = get_object_or_404(Deck, pk=deck_id)

    if request.method == 'POST':
        # Remove the deck from chosen decks
        request.user.profile.chosen_decks.remove(deck)

        # Synchronize UserDeck cards
        request.user.profile.user_deck.update_cards()

        # Delete progress entries for cards no longer in the UserDeck
        cards_to_remove = deck.cards.all()
        UserCardProgress.objects.filter(user=request.user, card__in=cards_to_remove).delete()
        
        messages.success(request, f'"{deck.name}" has been removed from your curriculum and progress has been deleted.')

        # Clear the dashboard cache to reflect changes
        cache_key = f'dashboard_data_{request.user.id}'
        cache.delete(cache_key)

    return redirect('user_deck_list')
