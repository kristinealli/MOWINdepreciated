from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cards.models import UserCardProgress


# Cards are handled by the UserDeck model, curriculum is handled by the chosen_decks field in the Profile model. 
@login_required
def dashboard_view(request):
    # Fetch user profile and decks
    user = request.user
    profile = user.profile

    # Check for due cards, created at first login
    first_login = False
    if not profile.chosen_decks.exists():
        first_login = True
        
    user_decks = profile.chosen_decks.all()  # Chosen decks by the user

    # Calculate due cards
    user_card_progresses = UserCardProgress.objects.filter(user=user)
    due_cards = [ucp for ucp in user_card_progresses if ucp.due_for_review()]
    count_due_cards = len(due_cards) 
    
    # Calculate mastery progress
    deck_stats = []
    for deck in user_decks:
        mastery_level = deck.get_progress(user)
        count_due_cards_in_deck = sum(1 for card in due_cards if card.card.deck == deck)
        cards_in_deck = deck.cards.count()
        deck_stats.append({
            'deck': deck,
            'mastery_level': mastery_level,
            'count_due_cards_in_deck': count_due_cards_in_deck,
            'cards_in_deck': cards_in_deck, 
        })

    # Calculate box distribution
    total_box_distribution = {
        box: UserCardProgress.objects.filter(user=user, box_level=box).count() or 0
        for box in range(1, 6)
    }

    # Render the dashboard template
    return render(request, 'cards/dashboard.html', {
        'user_decks': user_decks,
        'first_login': first_login,
        'count_due_cards': count_due_cards,
        'due_cards': due_cards,
        'deck_stats': deck_stats,
        'total_box_distribution': total_box_distribution,
        'box_levels': {1: "Learning", 2: "Revisiting", 3: "Mastering", 4: "Expert", 5: "Review"},
    })

def cards_in_box(request, box_level): 
    user = request.user      
    cards = UserCardProgress.objects.filter(user=user, box_level=box_level) 
    return render(request, 'cards/cards_in_box.html', {'cards_in_box': cards, 'box_level': box_level}) 