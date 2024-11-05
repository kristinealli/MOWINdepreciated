from django.views.generic import (ListView, CreateView, UpdateView, DetailView, View, TemplateView)
from .models import Card
from django.urls import (reverse_lazy, reverse)
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CardCheckForm
import random
from django.views import View

class CardListView(ListView):
    model = Card
    # Sort by 'subject' first, then 'box', and then '-date_created'
    queryset = Card.objects.all().order_by('subject', 'box', '-date_created')

class CardCreateView(CreateView):
    model = Card
    template_name = "cards/card_form.html"
    fields = ["anishinaabemowin", "english", "subject"]
    
    def form_valid(self, form):
        messages.success(self.request, "Card created successfully! Create another card below.")
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the same form to allow creating another card
        return reverse('card-create')
        
class CardUpdateView(UpdateView):
    model = Card
    template_name = "cards/card_form.html"
    fields = ["anishinaabemowin", "english", "subject"]

    def form_valid(self, form):
        messages.success(self.request, "Card updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the card list after updating
        return reverse('card-list')
        
class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"]= random.choice(self.object_list)
        return context
        
    def post (self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])
            
        return redirect(request.META.get("HTTP_REFERER"))
        
class PreviousCardView(View):
    def get(self, request, pk, *args, **kwargs):
        # Logic to get the previous card
        previous_card = Card.objects.filter(id__lt=pk).order_by('-id').first()
        if previous_card:
            return redirect('card-detail', pk=previous_card.id)
        return redirect('card-list')  # Redirect to card list if no previous card

class NextCardView(View):
    def get(self, request, pk, *args, **kwargs):
        # Logic to get the next card
        next_card = Card.objects.filter(id__gt=pk).order_by('id').first()
        if next_card:
            return redirect('card-detail', pk=next_card.id)
        return redirect('card-list')  # Redirect to card list if no next card
        
class CardDetailView(DetailView):
    model = Card
    template_name = "cards/card.html"  # Make sure to create this template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data if needed
        return context

class AboutView(TemplateView):
    template_name = "cards/about.html"
    
class DeckListView(View):
    template_name = "cards/decks.html"

    def get(self, request):
        # Get unique subjects from cards
        subjects = Card.objects.values_list('subject', flat=True).distinct()
        return render(request, self.template_name, {'subjects': subjects})

class DeckDetailView(ListView):
    template_name = "cards/deck_detail.html"
    context_object_name = 'cards'

    def get_queryset(self):
        # Filter cards by the subject in the URL
        return Card.objects.filter(subject=self.kwargs['subject'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = self.kwargs['subject']
        return context

class DeckCreateView(View):
    def post(self, request):
        subject = request.POST.get('subject')
        if subject:
            # Only add a new deck if a subject is provided
            if not Card.objects.filter(subject=subject).exists():
                # Create a placeholder card for the new deck
                Card.objects.create(
                    anishinaabemowin="Placeholder",
                    english="Placeholder",
                    subject=subject,
                    box=1
                )
        return redirect('deck-list')