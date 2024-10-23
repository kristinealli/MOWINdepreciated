from django.views.generic import ListView
from .models import Card

class CardListView(ListView):
    model = Card
    # Sort by 'subject' first, then 'box', and then '-date_created'
    queryset = Card.objects.all().order_by('subject', 'box', '-date_created')
