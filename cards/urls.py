from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

def staff_check(user):
    return user.is_staff or user.is_superuser

from .views import (
    AboutView,
    CardDetailView,
    CardListView,
    DeckListView,
    NextCardView,
    PreviousCardView,
    ProfileDetailView,
    ProfileUpdateView,
    signup,
    study_session,
    upload_cards,
    dashboard,
    home,
    profile_setup,
    add_to_curriculum, 
    remove_from_curriculum,
    deck_stats,
    curriculum_view, 
    CardsInDeckView, 
    user_progress_log,
    cards_in_box,
)


urlpatterns = [
    # General paths
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', dashboard, name='dashboard'),

    # Authentication paths
    path('login/', auth_views.LoginView.as_view(template_name='cards/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', signup, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Profile paths
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/setup/', profile_setup, name='profile-setup'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),


    # Deck paths
    path('decks/', DeckListView.as_view(), name='deck-list'),
    path('deck/<int:pk>/cards/', CardsInDeckView.as_view(), name='cards-in-deck'),
    path('deck/<int:pk>/stats/', deck_stats, name='deck-stats'),
    
    # Curriculum paths
    path('curriculum/', curriculum_view, name='curriculum'),
    path('deck/<int:pk>/add-to-curriculum/', add_to_curriculum, name='add-to-curriculum'),
    path('deck/<int:pk>/remove-from-curriculum/', remove_from_curriculum, name='remove-from-curriculum'),

    # Card paths
    path('card-list', CardListView.as_view(), name="card-list"),
    path('decks/<str:subject>/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('decks/<str:subject>/<int:pk>/previous/', PreviousCardView.as_view(), name='previous-card'),
    path('decks/<str:subject>/<int:pk>/next/', NextCardView.as_view(), name='next-card'),

    # Study and Review paths
    path('deck/<int:deck_pk>/study/', study_session, name='study_session'),

    # Upload paths (staff only)
    path('deck/<int:deck_pk>/upload/', upload_cards, name='upload-cards'),
    path('upload/', user_passes_test(staff_check)(upload_cards), name='upload-cards'),
    
    path('progress-log/', user_progress_log, name='user_progress_log'),
    path('cards-in-box/<int:box_level>/', cards_in_box, name='cards_in_box'),

]
