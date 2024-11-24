# Django imports
from django.contrib.auth import login
from django.shortcuts import redirect, render
from cards.forms import CustomUserCreationForm

# Authentication Views
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cards/signup.html', {'form': form})
