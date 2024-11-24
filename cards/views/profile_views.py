# Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, View, DetailView
from cards.forms import ProfileForm
from cards.models import Profile, UserCardProgress, Deck

# Profile Views
class ProfileDetailView(DetailView):
    template_name = 'cards/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        chosen_decks = user.profile.chosen_decks.all()

        # Filter decks with mastered cards
        mastered_decks = chosen_decks.filter(
            cards__usercardprogress__user=user,
            cards__usercardprogress__card_mastered=True
        ).distinct()

        # Count the number of mastered decks
        mastered_decks_count = mastered_decks.count()

        context['mastered_decks'] = mastered_decks
        context['mastered_decks_count'] = mastered_decks_count
        return context

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


