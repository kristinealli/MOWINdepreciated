from django.shortcuts import redirect, render
from django.views.generic import TemplateView

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
