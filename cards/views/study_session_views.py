# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.db import transaction 

# Local application imports
from cards.models import UserCardProgress, UserDeck, Card

# Define review intervals for the box system
review_intervals = {
    1: 0,    # Box 1: Reviewed immediately
    2: 1,    # Box 2: Reviewed after 1 day
    3: 3,    # Box 3: Reviewed after 3 days
    4: 7,    # Box 4: Reviewed after 7 days
    5: 14    # Box 5: Reviewed after 14 days
}

def update_review_log(current_progress, correct):
    # Update the review log
    if not isinstance(current_progress.review_log, list):
        current_progress.review_log = []
    current_progress.review_log.append({
        "date": current_progress.last_reviewed.isoformat(),
        "card_id": current_progress.card.id, 
        "box_level": current_progress.box_level,
        "progression": "yes" if correct else "no",  
    })
    current_progress.save(update_fields=['review_log']) 

@login_required
def study_session(request, card_id):
    current_progress = get_object_or_404(UserCardProgress, card_id=card_id, user=request.user)
    current_card = current_progress.card

    # Calculate total due cards at the start of the session
    total_due_cards = UserCardProgress.objects.filter(
        user=request.user,
        next_review_date__lte=timezone.now()
    ).count()

    if request.method == 'POST':
        correct = request.POST.get('correct') == 'true'
        current_progress.last_reviewed = timezone.now()

        if correct:
            # Move to the next box if correct, unless already in the last box
            if current_progress.box_level < 5:
                new_box_level = current_progress.box_level + 1
            else:
                new_box_level = current_progress.box_level
                current_progress.card_mastered = True
            # Update next review date based on the new box level
            next_review_interval = review_intervals[new_box_level]
        else:
            # Move to box 1 if incorrect
            new_box_level = 1
            # Set the next review date to the next day
            next_review_interval = 1

        with transaction.atomic():
            current_progress.next_review_date = current_progress.last_reviewed + timezone.timedelta(days=next_review_interval)
            update_review_log(current_progress, correct)
            current_progress.box_level = new_box_level
            current_progress.save()

        # Find the next due card
        next_due_card = UserCardProgress.objects.filter(
            user=request.user,
            next_review_date__lte=timezone.now()
        ).exclude(id=current_progress.id).first()

        if next_due_card:
            return redirect('study_session', card_id=next_due_card.card.id)
        else:
            return redirect('dashboard')  # Redirect to dashboard if no more due cards

    due_cards = UserCardProgress.objects.filter(user=request.user, next_review_date__lte=timezone.now())

    context = {
        'due_cards': due_cards, 
        'current_card': current_card,
        'cards_due': due_cards.count(),
        'total_due_cards': total_due_cards,
        'box_counts': {
            box: UserCardProgress.objects.filter(
                user=request.user,
                card__deck=current_card.deck,
                box_level=box
            ).count()
            for box in range(1, 6)
        }
    }
    return render(request, 'cards/study_session.html', context)
    