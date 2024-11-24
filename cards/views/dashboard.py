# Django imports
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render

# Local imports
from cards.models import UserCardProgress


@login_required
def dashboard(request):
    user = request.user
    profile = user.profile
    now = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Get the user's decks
    user_decks = profile.chosen_decks.all()
    print(user_decks) 

    # Calculate cards due today
    due_cards = []
    for deck in user_decks:
        due_cards.extend(deck.get_due_cards(user))
    print(due_cards)
    count_due_cards = len(due_cards)
    print(count_due_cards)

    # Aggregate box-level counts
    total_box_distribution = {
        box_level: len(set(
            UserCardProgress.objects.filter(
                user=user,
                card__deck__in=user_decks,
                box_level=box_level
            ).values_list('card_id', flat=True)
        ))
        for box_level in range(1, 6)
    }

    # Prepare context data
    context = {
        "user": user,
        "preferred_name": profile.preferred_name if profile.preferred_name else user.username,
        "user_decks": user_decks,
        "shared_decks": profile.shared_decks.all() if hasattr(profile, 'shared_decks') else [],
        "due_cards": due_cards,
        "count_due_cards": count_due_cards,
        "total_box_distribution": total_box_distribution,
        "box_levels": {
            1: 'Daily',
            2: '3 Days',
            3: 'Weekly',
            4: 'Biweekly',
            5: 'Monthly'
        },
        "first_login": request.session.get("first_login", False),
    }

    return render(request, 'cards/dashboard.html', context)


@login_required
def user_progress_log(request):
    user = request.user
    now = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Get today's progress log
    todays_progress_log = UserCardProgress.objects.filter(
        user=user,
        last_reviewed__gte=today_start
    ).select_related('card__deck')

    context = {
        'todays_progress_log': todays_progress_log,
    }

    return render(request, 'cards/user_progress_log.html', context)


@login_required
def cards_in_box(request, box_level):
    user = request.user
    user_decks = user.profile.chosen_decks.all()

    # Filter progress records for the specified box level
    progress_records_in_box = UserCardProgress.objects.filter(
        user=user,
        card__deck__in=user_decks,
        box_level=box_level
    ).select_related('card__deck').distinct('card_id')

    context = {
        'box_level': box_level,
        'cards_in_box': progress_records_in_box,
    }

    return render(request, 'cards/cards_in_box.html', context)


def user_deck_stats(request):
    user = request.user
    user_decks = user.profile.chosen_decks.all()
    deck_stats = []

    # Get deck statistics
    for deck in user_decks:
        mastery_level = round(deck.get_progress(user))
        due_cards = deck.get_due_cards(user)
        
        deck_stats.append({
            'deck': deck,
            'mastery_level': mastery_level,
            'due_cards': due_cards,
        })

    return deck_stats
