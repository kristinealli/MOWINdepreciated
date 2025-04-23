# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from cards.models import Deck
import logging

logger = logging.getLogger(__name__)

# Deck Views
class DeckListView(LoginRequiredMixin, ListView):
    """Display a simple list of all available flashcard decks."""
    model = Deck
    template_name = "cards/deck_list.html"
    context_object_name = 'decks'

    def get_queryset(self):
        queryset = Deck.objects.all().order_by('name')
        logger.debug("Number of decks fetched: %d", queryset.count())
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug("Rendering DeckListView with %d decks", len(context['decks']))
        context['show_add_buttons'] = self.request.GET.get('filter') == 'new'
        return context

class CardsInDeckView(LoginRequiredMixin, DetailView):
    """Display all cards within a specific deck."""
    model = Deck
    template_name = 'cards/cards_in_deck.html'
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Prefetch related card objects to optimize query
        deck = self.object
        deck = Deck.objects.prefetch_related('cards').get(id=deck.id)
        
        context['cards'] = deck.cards.all().order_by('english')
        
        # Use lazy % formatting in logging functions
        logger.debug("Deck: %s, Number of cards fetched: %d", deck.name, context['cards'].count())
        
        return context



