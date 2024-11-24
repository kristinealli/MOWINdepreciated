# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from cards.models import Deck

# Deck Views
class DeckListView(LoginRequiredMixin, ListView):
    """Display a simple list of all available flashcard decks."""
    model = Deck
    template_name = "cards/deck_list.html"
    context_object_name = 'decks'

    def get_queryset(self):
        if self.request.GET.get('filter') == 'new':
            return Deck.objects.exclude(
                id__in=self.request.user.profile.chosen_decks.values_list('id', flat=True)
            )
        return Deck.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_buttons'] = self.request.GET.get('filter') == 'new'
        return context

class CardsInDeckView(LoginRequiredMixin, DetailView):
    """Display all cards within a specific deck."""
    model = Deck
    template_name = 'cards/cards_in_deck.html'
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = self.object.cards.all().order_by('english')
        
        # Debugging: Print the number of cards fetched
        print(f"Deck: {self.object.name}, Number of cards fetched: {context['cards'].count()}")
        
        return context

