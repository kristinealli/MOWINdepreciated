"""
Tracks user progress on individual cards, including box level and review history.

"""

# Standard library imports
import json
import random
import csv

# Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    View,
    TemplateView,
    FormView
)
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.db.models import Q, OuterRef, Count, Sum
from django.contrib.auth.models import User  
from django.db import models 
from datetime import timedelta


# Local imports
from cards.models import Card, Deck, UserDeck, UserCardProgress, Profile, DeckShare
from .forms import FileUploadForm, CardForm, ProfileForm, CustomUserCreationForm


# Utility Functions
def calculate_card_progress(user, card):
    """
    Calculate user's progress for a specific card.

    Args:
        user: The user whose progress is being checked
        card: The card to check progress for

    Returns:
        int: The box level (1 if no progress exists)
    """
    progress = UserCardProgress.objects.filter(user=user, card=card).first()
    return progress.box_level if progress else 1

# Basic Views
class AboutView(TemplateView):
    """Display the about page for the flashcard application."""
    template_name = "cards/about.html"

class SignUpView(CreateView):
    """Handle user registration with custom form including preferred name."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cards/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        
        # Update profile with preferred name from form
        user.profile.preferred_name = form.cleaned_data.get('preferred_name')
        user.profile.save()

        messages.success(self.request, 'Account created successfully! Please login.')
        return response

# Deck Views
class DeckListView(LoginRequiredMixin, ListView):
    """Display a simple list of all available flashcard decks."""
    model = Deck
    template_name = "cards/deck_list.html"
    context_object_name = 'decks'

    def get_queryset(self):
        return Deck.objects.filter(
            Q(owner=self.request.user) | Q(is_public=True)
        ).order_by('name')

class UserDeckListView(LoginRequiredMixin, ListView):
    """Display a list of all decks added to the user's curriculum."""
    model = Deck
    template_name = "cards/user_deck_list.html"
    context_object_name = 'decks'   
    
    def get_queryset(self):
        # Get decks from user's chosen_decks in their profile
        return self.request.user.profile.chosen_decks.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all available decks for adding to curriculum
        context['available_decks'] = Deck.objects.filter(
            Q(is_public=True) | Q(owner=self.request.user)
        ).exclude(
            id__in=self.request.user.profile.chosen_decks.values_list('id', flat=True)
        ).order_by('-date_created')
        return context

@login_required
def curriculum_view(request):
    # Get user's chosen decks
    chosen_decks = request.user.profile.chosen_decks.all()
    
    context = {
        'chosen_decks': chosen_decks,
    }
    return render(request, 'cards/curriculum.html', context)

@login_required
def add_to_curriculum(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        request.user.profile.chosen_decks.add(deck)
        messages.success(request, f'"{deck.name}" has been added to your curriculum.')
    return redirect('curriculum')  # Now this will work

@login_required
def remove_from_curriculum(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        request.user.profile.chosen_decks.remove(deck)
        messages.success(request, f'"{deck.name}" has been removed from your curriculum.')
    return redirect('curriculum')  # Now this will work

class DeckDetailView(ListView):
    """Display all cards within a specific deck/subject."""
    template_name = "cards/deck_detail.html"
    context_object_name = 'cards'

    def get_queryset(self):
        """
        Filter cards by the specified subject.

        Returns:
            QuerySet: Cards filtered by subject
        """
        return Card.objects.filter(subject=self.kwargs['subject'])

    def get_context_data(self, **kwargs):
        """
        Add subject and deck to the context for template rendering.

        Returns:
            dict: Context dictionary with added subject and deck
        """
        context = super().get_context_data(**kwargs)
        context['subject'] = self.kwargs['subject']
        # Get the deck object
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs.get('pk'))
        return context

class DeckCreateView(LoginRequiredMixin, CreateView):
    """Handle creation of new decks with a placeholder card."""
    model = Deck
    fields = ['name', 'description', 'category', 'tags', 'is_public']
    success_url = reverse_lazy('deck-list')

    def form_valid(self, form):
        """
        Process valid form and show success message.

        Returns:
            HttpResponse: Redirect to success URL
        """
        messages.success(
            self.request,
            "Deck created successfully! Create another deck by clicking above."
        )
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get URL to redirect to after successful creation.

        Returns:
            str: URL for deck detail view
        """
        return reverse('deck-detail', kwargs={'subject': self.object.subject})

class DeckDeleteView(View):
    """Handle deletion of entire decks and their associated cards."""
    def post(self, request, subject):
        """
        Delete all cards associated with a subject/deck.

        Returns:
            HttpResponseRedirect: Redirect to deck list with success/error message
        """
        cards = Card.objects.filter(subject=subject)
        if cards.exists():
            cards.delete()
            messages.success(request, f"Deck '{subject}' deleted successfully.")
        else:
            messages.error(request, f"No deck found with the subject '{subject}'.")
        return redirect(reverse('deck-list'))

# Card Views
class CardListView(ListView):
    """Display all flashcards, ordered by subject, box, and creation date."""
    model = Card
    queryset = Card.objects.all().order_by('subject', '-date_created')

    def get_queryset(self):
        """
        Override get_queryset to include user-specific card progress information
        """
        base_queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # Annotate cards with their box level for the current user
            return base_queryset.annotate(
                box_level=models.Subquery(
                    UserCardProgress.objects.filter(
                        user=self.request.user,
                        card=OuterRef('pk')
                    ).values('box_level')[:1]
                )
            ).order_by('subject', 'box_level', '-date_created')
        return base_queryset

class CardDetailView(DetailView):
    """Display a single card with navigation to previous and next cards in the deck."""
    model = Card
    template_name = "cards/card_detail.html"

    def get_context_data(self, **kwargs):
        """
        Add previous and next card navigation context.

        Returns:
            dict: Context with previous_card and next_card
        """
        context = super().get_context_data(**kwargs)
        card = self.get_object()
        subject = card.subject
        deck_cards = Card.objects.filter(subject=subject).order_by("id")
        current_index = list(deck_cards).index(card)
        context["previous_card"] = (
            deck_cards[current_index - 1] if current_index > 0 else None
        )
        context["next_card"] = (
        deck_cards[current_index + 1] if current_index < len(deck_cards) - 1 else None
        )
        return context

@method_decorator(login_required, name='dispatch')
class CardCreateView(LoginRequiredMixin, CreateView):
    """Handle creation of new flashcards within a specific deck."""
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"

    def get_form_kwargs(self):
        """
        Add current subject to form kwargs.

        Returns:
            dict: Updated form kwargs including current_subject
        """
        kwargs = super().get_form_kwargs()
        kwargs["current_subject"] = self.request.GET.get("subject")
        return kwargs

    def form_valid(self, form):
        """
        Process valid form and show success message.

        Returns:
            HttpResponse: Redirect to success URL
        """
        messages.success(
            self.request,
            "Card created successfully! Create another card by clicking above."
        )
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get URL to redirect to after successful creation.

        Returns:
            str: URL for deck detail view
        """
        return reverse('deck-detail', kwargs={'subject': self.object.subject})

class CardUpdateView(LoginRequiredMixin, UpdateView):
    """Handle editing of existing flashcard content."""
    model = Card
    form_class = CardForm
    template_name = "cards/card_form.html"

    def get_success_url(self):
        """
        Get URL to redirect to after successful update.

        Returns:
            str: URL for deck detail view
        """
        return reverse('deck-detail', kwargs={'subject': self.object.subject})

class CardDeleteView(View):
    """Handle deletion of individual flashcards."""
    def post(self, request, pk):
        card = get_object_or_404(Card, id=pk)
        card.delete()
        messages.success(request, "Card deleted successfully!")
        return redirect('deck-detail', subject=card.subject)

# Study Session Views
class BoxView(LoginRequiredMixin, ListView):
    """Display cards filtered by their box number for spaced repetition study."""
    template_name = "cards/box.html"
    
    def get_queryset(self):
        return Card.objects.filter(
            usercardprogress__box_level=self.kwargs["box_number"],
            usercardprogress__user=self.request.user,
        ).order_by("usercardprogress__last_reviewed")

    def get_context_data(self, **kwargs):
        """
        Add box number and random check card to context.

        Returns:
            dict: Context with box_number and check_card
        """
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs.get("box_num")
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        context['subject'] = self.kwargs.get('subject')
        return context

class CardCheckView(View):
    """Process user responses during study sessions and move cards between boxes."""
    def post(self, request):
        """
        Process card check result and move card accordingly.

        Returns:
            HttpResponseRedirect: Redirect to card detail
        """
        card_id = request.POST.get('card_id')
        solved = request.POST.get('solved') == 'True'
        card = get_object_or_404(Card, id=card_id)
        card.move(solved)
        return redirect('card-detail', subject=card.subject, pk=card.id)

# Navigation Views
class PreviousCardView(View):
    """Navigate to the previous card in the current deck."""
    def get(self, _request, subject, pk):
        """
        Get previous card or wrap to last card.

        Returns:
            HttpResponseRedirect: Redirect to card detail
        """
        previous_card = (
            Card.objects.filter(subject=subject,
            id__lt=pk).order_by('-id').first()
        )
        if previous_card:
            return redirect('card-detail', subject=subject, pk=previous_card.id)
        last_card = Card.objects.filter(subject=subject).order_by('-id').first()
        return redirect('card-detail', subject=subject, pk=last_card.id)

class NextCardView(View):
    """Navigate to the next card in the current deck."""
    def get(self, _request, subject, pk):
        """
        Get next card or wrap to first card.

        Returns:
            HttpResponseRedirect: Redirect to card detail
        """
        next_card = (
        Card.objects.filter(subject=subject, id__gt=pk).order_by('id').first()
        )
        if next_card:
            return redirect('card-detail', subject=subject, pk=next_card.id)
        first_card = Card.objects.filter(subject=subject).order_by('id').first()
        return redirect('card-detail', subject=subject, pk=first_card.id)

# File Upload Views
class CardUploadView(FormView):
    """Handle bulk import of flashcards from JSON files."""
    template_name = "cards/upload.html"
    form_class = FileUploadForm
    success_url = reverse_lazy('deck-list')

    def form_valid(self, form):
        """
        Process valid form and create cards from file content.

        Returns:
            HttpResponse: Redirect to success URL
        """
        file = form.cleaned_data["file"]
        deck_name = form.cleaned_data["deck_name"]
        content = file.read().decode("utf-8")
        self.create_cards_from_content(content, deck_name)
        return super().form_valid(form)

    def create_cards_from_content(self, content, deck_name):
        """
        Create cards from JSON content.

        Args:
            content: JSON string containing card data
            deck_name: Name of the deck to create cards in
        """
        try:
            data = json.loads(content)
            for card_data in data:
                anishinaabemowin = card_data.get("anishinaabemowin")
                english = card_data.get("english")
                if anishinaabemowin and english:
                    Card.objects.create(
                        anishinaabemowin=anishinaabemowin,
                        english=english,
                        subject=deck_name,
                    )
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")

# Progress Tracking Functions
@login_required
def move_card(request, pk):
    """
    Move card to next box level.

    Args:
        request: HTTP request object
        pk: Primary key of the card

    Returns:
        HttpResponseRedirect: Redirect to previous page
    """
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.box += 1
        card.save()
    return redirect(request.META.get('HTTP_REFERER', 'card-list'))

@login_required
def add_to_study_deck(request, deck_id):
    """
    Add deck to user's study list.

    Args:
        request: HTTP request object
        deck_id: ID of the deck to add to study list

    Returns:
        HttpResponseRedirect: Redirect to study dashboard
    """
    deck = Deck.objects.get(id=deck_id)
    UserDeck.objects.get_or_create(user=request.user, deck=deck)
    return redirect('study_dashboard')

@login_required
def study_session(request, deck_pk):
    """
    Handle Leitner System study session for a deck.
    - Box 1: Review daily
    - Box 2: Every other day
    - Box 3: Every week
    - Box 4: Every two weeks
    - Box 5: Every month
    """
    deck = get_object_or_404(Deck, pk=deck_pk)
    
    # Get or create user's deck progress
    user_deck, _ = UserDeck.objects.get_or_create(
        user=request.user, 
        deck=deck
    )

    # Define review intervals for each box
    review_intervals = {
        1: timezone.timedelta(days=1),      # Box 1: Daily
        2: timezone.timedelta(days=2),      # Box 2: Every other day
        3: timezone.timedelta(days=7),      # Box 3: Weekly
        4: timezone.timedelta(days=14),     # Box 4: Bi-weekly
        5: timezone.timedelta(days=30),     # Box 5: Monthly
    }

    # Get cards due for review based on their box level and next review date
    due_cards = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        next_review_date__lte=timezone.now()
    ).order_by('box_level', 'next_review_date')

    # For new cards, create progress records in Box 1
    new_cards = deck.cards.exclude(
        usercardprogress__user=request.user
    )
    for card in new_cards:
        UserCardProgress.objects.create(
            user=request.user,
            card=card,
            box_level=1,  # Start in Box 1
            next_review_date=timezone.now()  # Due immediately
        )

    # Get current card to study
    current_card = None
    if due_cards.exists():
        current_progress = due_cards[0]
        current_card = current_progress.card
        
        # Handle POST request (card review)
        if request.method == 'POST':
            correct = request.POST.get('correct') == 'true'
            
            if correct:
                # Move to next box if not in box 5
                if current_progress.box_level < 5:
                    current_progress.box_level += 1
            else:
                # Move back to box 1 if incorrect
                current_progress.box_level = 1
            
            # Set next review date based on new box level
            current_progress.next_review_date = (
                timezone.now() + review_intervals[current_progress.box_level]
            )
            current_progress.save()
            
            # Redirect to next card
            return redirect('study_session', deck_pk=deck_pk)

    # Prepare context for template
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

@login_required
def update_card_progress(request, card_id):
    """
    Update user's progress on a specific card.

    Args:
        request: HTTP request object
        card_id: ID of the card to update

    Returns:
        HttpResponseRedirect: Redirect to study session
    """
    user_progress = UserCardProgress.objects.get(user=request.user, card_id=card_id)
    # Check if card has already moved to the next box in this round
    if not user_progress.round_completed:
        user_progress.box_level += 1
        user_progress.round_completed = True # Marks it as reviewed for the round

    # Save progress
    user_progress.last_reviewed = timezone.now()
    user_progress.save()
    return redirect('study_session') # Redirect to study session page

def start_study_session(request):
    """
    Reset rounds for the user starting a new session.

    Returns:
        HttpResponse: Rendered study session template
    """
    # Reset rounds for the user starting a new session
    UserCardProgress.objects.filter (
        user=request.user,
        round_completed=True
    ).update(round_completed=False)

    # Now load the study session with a fresh round
    decks = get_user_decks(request.user)
    return render(request, 'study_session.html', {'decks': decks})

def get_user_decks(user):
    """
    Get decks for a specific user.

    Args:
        user: User object

    Returns:
        QuerySet: Decks for the user
    """
    return UserDeck.objects.filter(user=user).values_list('deck', flat=True)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard' )
    else:
        form = CustomUserCreationForm()
    return render(request, 'cards/signup.html', {'form': form})

@login_required
def profile_setup(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'cards/profile_setup.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'form': profile_form,
        'user': request.user,
        'profile': request.user.profile
    }
    return render(request, 'cards/profile.html', context)

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'profile_user': user,
        'profile': user.profile
    }
    return render(request, 'cards/profile_view.html', context)

def home(request):
    """
    Render the home page.
    If user is authenticated, redirect to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'cards/home.html')

@login_required
def study_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    user_deck = get_object_or_404(UserDeck, user=request.user, deck=deck)
    
    # Calculate total reviews
    total_reviews = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck
    ).count()
    
    # Calculate cards due for review
    now = timezone.now()
    cards_due = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        next_review_date__lte=now
    ).count()
    
    # Get total cards in deck
    total_cards = deck.cards.count()
    
    # Calculate mastered cards (cards in box 5)
    mastered_cards = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        box_level=5
    ).count()
    
    # Calculate accuracy if there are reviews
    if total_reviews > 0:
        correct_reviews = UserCardProgress.objects.filter(
            user=request.user,
            card__deck=deck,
            correct_count__gt=0
        ).aggregate(
            total_correct=Sum('correct_count')
        )['total_correct'] or 0
        accuracy = (correct_reviews / total_reviews) * 100
    else:
        accuracy = 0
    
    # Get next review time
    next_review = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        next_review_date__gt=now
    ).order_by('next_review_date').first()
    
    # Calculate box distribution
    box_distribution = {
        box: UserCardProgress.objects.filter(
            user=request.user,
            card__deck=deck,
            box_level=box
        ).count()
        for box in range(6)  # Boxes 0-5
    }
    
    box_levels = list(range(6))  # [0, 1, 2, 3, 4, 5]
    
    # Get study history (last 7 days)
    seven_days_ago = now - timedelta(days=7)
    study_history = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        last_reviewed__gte=seven_days_ago
    ).values('last_reviewed__date').annotate(
        reviews=Count('id')
    ).order_by('last_reviewed__date')
    
    # Format study stats
    study_stats = {
        stat.last_reviewed__date: stat.reviews
        for stat in study_history
    }

    context = {
        'deck': deck,
        'user_deck': user_deck,
        'cards_studied': total_reviews,
        'cards_due': cards_due,
        'total_cards': total_cards,
        'mastered_cards': mastered_cards,
        'accuracy': accuracy,
        'next_review': next_review.next_review_date if next_review else None,
        'box_distribution': box_distribution,
        'box_levels': box_levels,
        'study_stats': study_stats,
        'study_history': study_history,
    }
    
    return render(request, 'cards/study_session.html', context)

@login_required
def upload_cards(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)

    # Check if user has permission to modify this deck
    if deck.owner != request.user:
        messages.error(request, 'You do not have permission to modify this deck.')
        return redirect('deck-detail', pk=deck_pk)

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Process CSV file
                decoded_file = file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    Card.objects.create(
                        deck=deck,  # Add this to associate card with deck
                        anishinaabemowin=row['anishinaabemowin'],
                        english=row['english'],
                        pronunciation=row.get('pronunciation', ''),
                        subject=row.get('subject', deck.name)  # Default to deck name if not provided
                    )
                messages.success(request, f'Cards successfully uploaded to {deck.name}!')
                return redirect('deck-detail', pk=deck_pk)
            except (csv.Error, UnicodeDecodeError, KeyError) as e:
                messages.error(request, f'Error processing file: {str(e)}')
    else:
        form = FileUploadForm()

    return render(request, 'cards/upload_cards.html', {
        'form': form,
        'deck': deck
    })

@login_required
def dashboard(request):

    # Get user's decks with progress
    user_decks = request.user.profile.chosen_decks.all().annotate(
        total_cards=models.Count('cards'),
        mastered_cards=models.Count(
            'cards',
            filter=models.Q(
                usercardprogress__user=request.user,
                usercardprogress__box_level=5  # Box 5 represents mastered cards
            )
        ),
        cards_due=models.Count(
            'cards',
            filter=models.Q(
                usercardprogress__user=request.user,
                usercardprogress__next_review_date__lte=timezone.now()
            )
        ),
        last_reviewed=models.Max('usercardprogress__last_reviewed')
    ).order_by('-date_created')

    # Count cards due for review
    cards_due = UserCardProgress.objects.filter(
        user=request.user,
        next_review_date__lte=timezone.now()
    ).count()

    # Get first deck with due cards
    first_due_deck = None
    if cards_due > 0:
        first_due_progress = UserCardProgress.objects.filter(
            user=request.user,
            next_review_date__lte=timezone.now()
        ).first()
        if first_due_progress:
            first_due_deck = first_due_progress.card.decks.first()

    # Today's stats
    today_reviews_count = UserCardProgress.objects.filter(
        user=request.user,
        last_reviewed__date=timezone.now().date()
    ).count()
    
    # Calculate today's accuracy using box_level changes instead
    today_correct_reviews = UserCardProgress.objects.filter(
        user=request.user,
        last_reviewed__date=timezone.now().date(),
        last_review_result=True  # Use the boolean field that tracks if the review was correct
    ).count()
    
    today_accuracy = (today_correct_reviews / today_reviews_count * 100) if today_reviews_count > 0 else 0
    
    # Shared decks
    shared_decks = DeckShare.objects.filter(
        shared_with=request.user,
        active=True
    ).select_related('deck')[:5]

    # Box distribution
    box5_cards = get_box_count(request.user, 5)
    box4_cards = get_box_count(request.user, 4)
    box3_cards = get_box_count(request.user, 3)
    box2_cards = get_box_count(request.user, 2)
    box1_cards = get_box_count(request.user, 1)
    total_cards = box5_cards + box4_cards + box3_cards + box2_cards + box1_cards

    context = {
        'user_decks': user_decks,
        'cards_due': cards_due,
        'first_due_deck': first_due_deck,
        
        # Today's stats
        'today_reviews_count': today_reviews_count,
        
        'today_accuracy': today_accuracy,
        
        # Shared decks
        'shared_decks': shared_decks,
            
        # Box distribution
        'box5_cards': box5_cards,
        'box4_cards': box4_cards,
        'box3_cards': box3_cards,
        'box2_cards': box2_cards,
        'total_cards': total_cards,
    }

    return render(request, 'cards/dashboard.html', context)

@login_required
def dashboard(request):
    # Get user's decks and shared decks
    user_decks = request.user.profile.chosen_decks.all()
    shared_decks = DeckShare.objects.filter(shared_with=request.user)

    # Set the start of today (midnight)
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Get all reviews done today
    today_reviews = UserCardProgress.objects.filter(
        user=request.user,
        last_reviewed__gte=today_start  # greater than or equal to midnight today
    )

    # Count total reviews today
    today_reviews_count = today_reviews.count()

    # Count correct reviews today
    today_correct = today_reviews.filter(last_review_result=True).count()

    # Calculate accuracy percentage
    # If there are reviews, calculate (correct/total * 100), otherwise return 0
    today_accuracy = round((today_correct / today_reviews_count * 100) if today_reviews_count > 0 else 0)

    # Get due cards based on Leitner system
    due_cards = UserCardProgress.objects.filter(
        user=request.user,
        next_review_date__lte=timezone.now()
    ).select_related('card__deck').order_by('box_level', 'next_review_date')

    first_due_progress = due_cards.first()
    cards_due = due_cards.count()

    # Get deck statistics with Leitner box distribution
    user_deck_stats = []  # Renamed from deck_stats
    for deck in user_decks:
        # Get progress for this deck
        deck_progress = UserCardProgress.objects.filter(
            user=request.user,
            card__deck=deck
        )
        
        # Calculate deck statistics
        total_cards = deck.cards.count()
        cards_studied = deck_progress.count()
        progress = round((cards_studied / total_cards * 100) if total_cards > 0 else 0)
        
        # Calculate box distribution
        box_distribution = {
            1: deck_progress.filter(box_level=1).count(),
            2: deck_progress.filter(box_level=2).count(),
            3: deck_progress.filter(box_level=3).count(),
            4: deck_progress.filter(box_level=4).count(),
            5: deck_progress.filter(box_level=5).count(),
        }
        
        # Calculate mastery (cards in boxes 4 and 5)
        mastered_cards = box_distribution[4] + box_distribution[5]
        mastery_level = round((mastered_cards / total_cards * 100) if total_cards > 0 else 0)
        
        # Get due cards for this deck
        due_cards_count = deck_progress.filter(
            next_review_date__lte=timezone.now()
        ).count()

        user_deck_stats.append({
            'deck': deck,
            'progress': progress,
            'mastery_level': mastery_level,
            'due_cards_count': due_cards_count,
            'box_distribution': box_distribution,
            'total_cards': total_cards,
            'cards_studied': cards_studied
        })

    context = {
        'user_decks': user_deck_stats,
        'shared_decks': shared_decks,
        'today_reviews_count': today_reviews_count,
        'today_accuracy': today_accuracy,
        'cards_due': cards_due,
        'has_due_cards': first_due_progress is not None,
        'first_due_deck': first_due_progress.card.deck if first_due_progress else None,
        'box_levels': {
            1: "Learning",
            2: "Review (1 day)",
            3: "Review (3 days)",
            4: "Review (1 week)",
            5: "Mastered (2 weeks)"
        }
    }
    
        # Calculate total box distribution across all decks
    total_box_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    
    # Get all progress records for the user
    progress_records = UserCardProgress.objects.filter(user=request.user)
    
    # Count cards in each box
    for box_level in range(1, 6):
        total_box_distribution[box_level] = progress_records.filter(
            box_level=box_level
        ).count()
    
    # Calculate total cards
    total_cards = sum(total_box_distribution.values())
    
    context.update({
        'total_box_distribution': total_box_distribution,
        'total_cards': total_cards,
        'box_levels': {
            1: 'Daily',
            2: '3 Days',
            3: 'Weekly',
            4: 'Biweekly',
            5: 'Monthly'
        }
    })
    
    return render(request, 'cards/dashboard.html', context)
    
@login_required
def profile_redirect(request):
    return redirect('profile-detail', username=request.user.username)

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'cards/profile_setup.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-detail', kwargs={'username': self.request.user.username})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'cards/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile-detail', kwargs={'username': self.request.user.username})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'cards/profile.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        return self.request.user

def get_box_count(user, box_level):
    """
    Get the count of cards in a specific box level for a user.
    
    Args:
        user: The user to check
        box_level: The box level to count (1-5)
        
    Returns:
        int: Number of cards in the specified box
    """
    return UserCardProgress.objects.filter(
        user=user,
        box_level=box_level
    ).count()

class ProfileSetupView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['preferred_name', 'chosen_decks']
    template_name = 'cards/profile_setup.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Get or create profile
        self.profile, created = Profile.objects.get_or_create(
            user=self.request.user,
            defaults={'preferred_name': self.request.user.username}
        )
        kwargs['instance'] = self.profile
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

@login_required
def review_card(request, deck_id, card_id):
    if request.method == 'POST':
        quality = int(request.POST.get('quality', 1))
        user_deck = get_object_or_404(UserDeck, 
            user=request.user, 
            deck_id=deck_id
        )
        card = get_object_or_404(Card, id=card_id)
        
        user_deck.process_review(card, quality)
        
        # Get next card or redirect to completion
        next_card = user_deck.start_study_session().first()
        if next_card:
            return redirect('review-card', deck_id=deck_id, card_id=next_card.id)
        return redirect('deck-complete', deck_id=deck_id)
    
    # ... handle GET request ...

@login_required
def deck_stats(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    user_deck = get_object_or_404(UserDeck, user=request.user, deck=deck)
    
    # Calculate statistics
    total_cards = deck.cards.count()
    mastered_cards = user_deck.mastered_cards.count()
    mastery_percentage = (mastered_cards / total_cards * 100) if total_cards > 0 else 0
    
    context = {
        'deck': deck,
        'user_deck': user_deck,
        'total_cards': total_cards,
        'mastered_cards': mastered_cards,
        'mastery_percentage': mastery_percentage,
    }
    
    return render(request, 'cards/deck_stats.html', context)

@login_required
def user_deck_list(request):
    # Get chosen decks from user's profile
    decks = request.user.profile.chosen_decks.all()
    print(f"Decks found: {decks.count()}")
    
    context = {
        'decks': decks,  # This will match your template's {% if decks %}
    }
    return render(request, 'cards/user_deck_list.html', context)

class CardsInDeckView(LoginRequiredMixin, DetailView):
    """Display all cards within a specific deck."""
    model = Deck
    template_name = 'cards/cards_in_deck.html'
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all cards in this deck
        context['cards'] = self.object.cards.all().order_by('english')
        return context
