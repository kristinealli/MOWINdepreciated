# Django imports
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.db.models import OuterRef
from django.db import models 
from cards.models import Card, UserCardProgress


# Card Views
class CardListView(ListView):
    """Display all flashcards, ordered by subject, box, and creation date."""
    model = Card
    queryset = Card.objects.all().order_by('subject', '-date_created')

    def get_queryset(self):
        """
        Override get_queryset to include user-specific card progress information.
        """
        base_queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return base_queryset.annotate(
                box_level=models.Subquery(
                    UserCardProgress.objects.filter(
                        user=self.request.user,
                        card=OuterRef('id')
                    ).values('box_level')[:1]
                )
            ).order_by('subject', 'box_level', '-date_created')
        return base_queryset

class CardDetailView(DetailView):
    """Display a single card with navigation to previous and next cards in the deck."""
    model = Card
    template_name = "cards/card_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = self.get_object()
        subject = card.subject
        deck_cards = Card.objects.filter(subject=subject).order_by("id")
        current_index = list(deck_cards).index(card)
        context["previous_card"] = deck_cards.filter(id__lt=card.id).order_by('-id').first()
        context["next_card"] = deck_cards.filter(id__gt=card.id).order_by('id').first()

        return context

class PreviousCardView(View):
    """Navigate to the previous card in the current deck."""
    def get(self, _request, subject, card_id):
        previous_card = (
            Card.objects.filter(subject=subject, id__lt=card_id).order_by('-id').first()
        )
        if previous_card:
            return redirect('card-detail', subject=subject, id=previous_card.id)
        last_card = Card.objects.filter(subject=subject).order_by('-id').first()
        return redirect('card-detail', subject=subject, id=last_card.id)

class NextCardView(View):
    """Navigate to the next card in the current deck."""
    def get(self, _request, subject, id):
        next_card = (
            Card.objects.filter(subject=subject, id__gt=id).order_by('id').first()
        )
        if next_card:
            return redirect('card-detail', subject=subject, id=next_card.id)
        first_card = Card.objects.filter(subject=subject).order_by('id').first()
        return redirect('card-detail', subject=subject, id=first_card.id)
