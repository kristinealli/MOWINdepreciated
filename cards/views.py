from django.views.generic import (ListView, CreateView, UpdateView, DetailView, View, TemplateView, FormView)
from django.urls import (reverse_lazy, reverse)
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CardCheckForm, FileUploadForm, CardForm
from .models import Card
import random

class CardDetailView(DetailView):
    model = Card
    template_name = "cards/card.html"  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CardListView(ListView):
    model = Card
    # Sort by 'subject' first, then 'box', and then '-date_created'
    queryset = Card.objects.all().order_by('subject', 'box', '-date_created')

class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"
    # fields = ["anishinaabemowin", "english", "subject"]
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Pass the current subject (deck) to the form
        kwargs["current_subject"] = self.request.GET.get("subject")
        return kwargs
    
    def form_valid(self, form):
        messages.success(self.request, "Card created successfully! Create another card by clicking above.")
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the same form to allow creating another card
        return reverse('deck-detail', kwargs={'subject': self.object.subject})

class CardUpdateView(UpdateView):
    model = Card
    template_name = "cards/card_form.html"
    fields = ["anishinaabemowin", "english", "subject"]

    def form_valid(self, form):
        messages.success(self.request, "Card updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'subject': self.object.subject})

class CardDeleteView(View):
    def post(self, request, pk):
        card = get_object_or_404(Card, id=pk)
        card.delete()
        messages.success(request, "Card deleted successfully!")
        return redirect('deck-detail', subject=card.subject)

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

class AboutView(TemplateView):
    template_name = "cards/about.html"

class DeckListView(View):
    template_name = "cards/decks.html"

    def get(self, request):
        subjects = Card.objects.values_list('subject', flat=True).distinct()
        return render(request, self.template_name, {'subjects': subjects})

class DeckDetailView(ListView):
    template_name = "cards/deck_detail.html"
    context_object_name = 'cards'

    def get_queryset(self):
        return Card.objects.filter(subject=self.kwargs['subject'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = self.kwargs['subject']
        return context

class DeckCreateView(View):
    def post(self, request):
        subject = request.POST.get('subject')
        if subject:
            if not Card.objects.filter(subject=subject).exists():
                Card.objects.create(
                    anishinaabemowin="Placeholder",
                    english="Placeholder",
                    subject=subject,
                    box=1
                )
        return redirect('deck-list')

class DeckDeleteView(View):
    def post(self, request, subject):
        cards = Card.objects.filter(subject=subject)
        
        if cards.exists():
            cards.delete()
            messages.success(request, f"Deck '{subject}' deleted successfully.")
        else:
            messages.error(request, f"No deck found with the subject '{subject}'.")
        return redirect(reverse('deck-list'))
        
class CardUploadView(FormView):
    template_name = "cards/upload.html"
    form_class = FileUploadForm  
    success_url = reverse_lazy('deck-list')

    def form_valid(self, form):
        file = form.cleaned_data["file"]
        deck_name = form.cleaned_data["deck_name"]
        content = file.read().decode("utf-8")
        self.create_cards_from_content(content, deck_name)
        return super().form_valid(form)

    def create_cards_from_content(self, content, deck_name):
        lines = content.strip().split("\n")
        for line in lines:
            parts = line.split(" ", 1)
            if len(parts) == 2:
                anishinaabemowin, english = parts[0].strip(), parts[1].strip()
                print(f"Creating card: {anishinaabemowin} - {english}")  # Debugging line

                Card.objects.create(
                    anishinaabemowin= anishinaabemowin,
                    english= english,
                    subject= deck_name
                )