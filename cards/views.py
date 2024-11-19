# Standard library imports
import json

# Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    View,
    TemplateView,
)
from django.contrib.auth import login
from django.db.models import OuterRef
from django.db import models 
from django.core.cache import cache
from django.core.exceptions import PermissionDenied


# Local imports
from cards.models import Card, Deck, UserDeck, UserCardProgress, Profile
from .forms import ProfileForm, CustomUserCreationForm

# General Views
def home(request):
    """
    Render the home page.
    If user is authenticated, redirect to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'cards/home.html')
    
class AboutView(TemplateView):
    """Display the about page for the flashcard application."""
    template_name = "cards/about.html"

@login_required
def dashboard(request):
    user = request.user
    now = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    user_decks = user.profile.chosen_decks.all()
    
    # Set first_login in session (used to influence Welcome message)
    if 'first_login' not in request.session:
        request.session['first_login'] = True
    else:
        request.session['first_login'] = False

    # Filter progress records to only include current user decks
    progress_records = UserCardProgress.objects.filter(
        user=user,
        card__deck__in=user_decks
    ).select_related('card__deck')  # Optimize related lookups
    
    # Get due cards, ensuring no duplicates
    due_cards = progress_records.filter(next_review_date__lte=now).order_by('card_id').distinct('card_id')
    
    # Count due cards
    cards_due = due_cards.count()
    
    # Get first due card
    first_due_progress = due_cards.select_related('card__deck').first()

    # Calculate total box distribution with distinct card counts
    total_box_distribution = {}
    for box_level in range(1, 6):
        total_box_distribution[box_level] = UserCardProgress.objects.filter(
            user=user,
            card__deck__in=user_decks,
            box_level=box_level
        ).order_by('card_id').distinct('card_id').count()

    # Get deck statistics with optimized queries
    user_deck_stats = []
    for deck in user_decks:
        # Filter progress records for this deck (reuse existing queryset)
        deck_progress = progress_records.filter(card__deck=deck)
        # Count total cards in deck 
        total_cards = deck.cards.count()
        # Calculate mastery level
        mastered_cards = deck_progress.filter(box_level__in=[4, 5]).count()
        mastery_level = round((mastered_cards / total_cards * 100) if total_cards > 0 else 0)
        # Calculate due cards for this deck
        due_cards_count = deck_progress.filter(next_review_date__lte=now).order_by('card_id').distinct('card_id').count()
        # Append deck stats to list for display in dashboard 
        user_deck_stats.append({
            'deck': deck,
            'mastery_level': mastery_level,
            'due_cards': due_cards_count,
        })
    
    # Dashboard data for display
    dashboard_data = {
        'user_decks': user_deck_stats,
        'today_reviews_count': progress_records.filter(
            last_reviewed__gte=today_start
        ).count(),
        'cards_due': cards_due,  # Total due cards across all decks
        'first_due_deck': first_due_progress.card.deck if first_due_progress else None,
        'total_box_distribution': total_box_distribution,
        'box_levels': {
            1: 'Daily',
            2: '3 Days',
            3: 'Weekly',
            4: 'Biweekly',
            5: 'Monthly'
        }
    }

    return render(request, 'cards/dashboard.html', dashboard_data)

# Authentication Views
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

class ProfileDetailView(LoginRequiredMixin, View):
    template_name = 'cards/profile.html'

    def get(self, request):
        context = {
            'user': request.user,
            'profile': request.user.profile,
            'form': ProfileForm(instance=request.user.profile),
            'total_cards': UserCardProgress.objects.filter(user=request.user).count(),
            'box_levels': range(1, 6),
            'progress_by_box': {
                box: UserCardProgress.objects.filter(
                    user=request.user,
                    box_level=box
                ).count() for box in range(1, 6)
            }
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')
        
        # If form is invalid, re-render with errors
        context = {
            'user': request.user,
            'profile': request.user.profile,
            'form': form,
            'total_cards': UserCardProgress.objects.filter(user=request.user).count(),
            'box_levels': range(1, 6),
            'progress_by_box': {
                box: UserCardProgress.objects.filter(
                    user=request.user,
                    box_level=box
                ).count() for box in range(1, 6)
            }
        }
        return render(request, self.template_name, context)    

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

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'cards/profile_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Check what changed and create appropriate message
        if 'preferred_name' in form.changed_data:
            new_name = form.cleaned_data['preferred_name']
            if new_name:
                messages.success(self.request, f'Your preferred name has been updated to "{new_name}".')
            else:
                messages.success(self.request, 'Your preferred name has been removed.')
        return response

    def get_object(self, queryset=None):
        return self.request.user.profile

# Deck Views
class DeckListView(LoginRequiredMixin, ListView):
    """Display a simple list of all available flashcard decks."""
    model = Deck
    template_name = "cards/deck_list.html"
    context_object_name = 'decks'

    def get_queryset(self):
        # Check if we're showing new decks only
        if self.request.GET.get('filter') == 'new':
            # Show decks not in user's chosen_decks
            return Deck.objects.exclude(
                id__in=self.request.user.profile.chosen_decks.values_list('id', flat=True)
            )
        # Show all decks
        return Deck.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add flag to indicate if we're showing new decks
        context['show_add_buttons'] = self.request.GET.get('filter') == 'new'
        return context

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

# Curriculum Views
@login_required
def curriculum_view(request):
    chosen_decks = request.user.profile.chosen_decks.all()
    all_decks = Deck.objects.all()
    available_decks = all_decks.exclude(id__in=chosen_decks.values_list('id', flat=True))

    context = {
        'decks': chosen_decks,
        'available_decks': available_decks,
    }
    return render(request, 'cards/user_deck_list.html', context)

@login_required
def add_to_curriculum(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        # Add deck to user's curriculum
        request.user.profile.chosen_decks.add(deck)
        
        # Create initial progress entries for all cards in this deck
        cards = deck.cards.all()
        now = timezone.now()
        
        # Check existing progress records to avoid duplicates
        existing_progress = UserCardProgress.objects.filter(user=request.user, card__in=cards)
        existing_card_ids = existing_progress.values_list('card_id', flat=True)
        
        # Bulk create progress entries for each card not already in progress
        new_progress = [
            UserCardProgress(
                user=request.user,
                card=card,
                box_level=1,  # All new cards start in box 1
                next_review_date=now,  # Due immediately
            ) for card in cards if card.id not in existing_card_ids
        ]
        
        UserCardProgress.objects.bulk_create(new_progress)
        
        print(f"Added {len(new_progress)} new progress records for deck '{deck.name}'")
        
        messages.success(request, f'"{deck.name}" has been added to your curriculum.')
        
    return redirect('dashboard')

@login_required
def remove_from_curriculum(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        request.user.profile.chosen_decks.remove(deck)
        messages.success(request, f'"{deck.name}" has been removed from your curriculum.')
        
        # Clear dashboard cache to ensure updated counts are shown
        cache_key = f'dashboard_data_{request.user.id}'
        cache.delete(cache_key)
        
    return redirect('curriculum')

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

# Study Session Views
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

    # Define review intervals for each box
    review_intervals = {
        1: timezone.timedelta(days=1),      # Box 1: Daily
        2: timezone.timedelta(days=2),      # Box 2: Every other day
        3: timezone.timedelta(days=7),      # Box 3: Weekly
        4: timezone.timedelta(days=14),     # Box 4: Bi-weekly
        5: timezone.timedelta(days=30),     # Box 5: Monthly
    }

    # First, create progress for new cards
    new_cards = deck.cards.exclude(usercardprogress__user=request.user)
    for card in new_cards:
        UserCardProgress.objects.create(
            user=request.user,
            card=card,
            box_level=1,
            next_review_date=timezone.now()
        )

    # Then, get all due cards (including newly created ones)
    due_cards = UserCardProgress.objects.filter(
        user=request.user,
        card__deck=deck,
        next_review_date__lte=timezone.now()
    ).order_by('box_level', 'next_review_date')

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
def upload_cards(request):
    # Check if user is staff or superuser
    if not request.user.is_staff and not request.user.is_superuser:
        raise PermissionDenied("You don't have permission to upload cards.")
        
    if request.method == 'POST':
        try:
            json_data = request.POST.get('json_data')
            if not json_data:
                messages.error(request, "Please provide JSON data.")
                return redirect('upload-cards')

            data = json.loads(json_data)
            
            # Create or update the deck
            deck, created = Deck.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data.get('description', ''),
                    'is_public': data.get('is_public', True)
                }
            )

            # Process cards
            cards_created = 0
            for card_data in data.get('cards', []):
                if all(key in card_data for key in ['anishinaabemowin', 'english']):
                    Card.objects.create(
                        deck=deck,
                        anishinaabemowin=card_data['anishinaabemowin'],
                        english=card_data['english'],
                        pronunciation=card_data.get('pronunciation', ''),
                        subject=deck.name  # Set subject to deck name by default
                    )
                    cards_created += 1

            if cards_created > 0:
                messages.success(
                    request,
                    f'Successfully created {cards_created} cards in deck "{deck.name}"!'
                )
            return redirect('deck-list')

        except json.JSONDecodeError as e:
            messages.error(request, f'Invalid JSON format: {str(e)}')
        except KeyError as e:
            messages.error(request, f'Missing required field: {str(e)}')
        except ValueError as e:
            messages.error(request, f'Error processing data: {str(e)}')

    return render(request, 'cards/upload.html')

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

    # Filter progress records for the specified box level and ensure no duplicates
    progress_records_in_box = UserCardProgress.objects.filter(
        user=user,
        card__deck__in=user_decks,
        box_level=box_level
    ).select_related('card__deck').order_by('card_id').distinct('card_id')

    context = {
        'box_level': box_level,
        'cards_in_box': progress_records_in_box,
    }

    return render(request, 'cards/cards_in_box.html', context)
