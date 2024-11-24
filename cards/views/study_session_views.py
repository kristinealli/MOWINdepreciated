# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from cards.models import Deck, UserCardProgress

# Define review intervals for the box system
review_intervals = {
    1: 0,    # Box 1: Reviewed immediately
    2: 1,    # Box 2: Reviewed after 1 day
    3: 3,    # Box 3: Reviewed after 3 days
    4: 7,    # Box 4: Reviewed after 7 days
    5: 14    # Box 5: Reviewed after 14 days
}

@login_required
def study_session(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)

    new_cards = deck.cards.exclude(usercardprogress__user=request.user)
    for card in new_cards:
        # Check if a UserCardProgress object already exists for this user and card
        if not UserCardProgress.objects.filter(user=request.user, card=card).exists():
            UserCardProgress.objects.create(
                user=request.user,
                card=card,
                box_level=1,
                next_review_date=timezone.now()
            )

    due_cards = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        next_review_date__lte=timezone.now()
    ).order_by('box_level', 'next_review_date')

    current_card = None
    if due_cards.exists():
        current_progress = due_cards[0]
        current_card = current_progress.card

        if request.method == 'POST':
            correct = request.POST.get('correct') == 'true'
            current_progress.last_reviewed = timezone.now()
            
            intervals = {1: 0, 2: 1, 3: 3, 4: 7, 5: 14}

            if correct:
                if current_progress.box_level == 5:
                    current_progress.card_mastered = True 
                    new_box_level = current_progress.box_level
                else:
                    new_box_level = min(current_progress.box_level + 1, 5)

            else:
                new_box_level = 1

            # Update next review date based on the new box level
            current_progress.next_review_date = current_progress.last_reviewed + timezone.timedelta(days=intervals[new_box_level])

            # Update the review log
            current_progress.review_log.append({
                "date": current_progress.last_reviewed.isoformat(),
                "card_id": current_progress.card.id, 
                "box_level": current_progress.box_level,
                "progression": "yes" if correct else "no",  
            })

            # Update the box level
            current_progress.box_level = new_box_level
            current_progress.save()  # Save all changes
            
            request.user.save()  # Save user changes

            return redirect('study_session', deck_id=deck_id)

    context = {
        'deck': deck,
        'current_card': current_card,
        'cards_due': due_cards.count(),
        'box_counts': {
            box: UserCardProgress.objects.filter(
                user=request.user,
                card__deck=deck,
                box_level=box
            ).count()
            for box in range(1, 6)
        }
    }
    return render(request, 'cards/study_session.html', context)