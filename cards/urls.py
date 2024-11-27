from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

from cards.views import * 

def staff_check(user):
    return user.is_staff or user.is_superuser


urlpatterns = [
    # General paths
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', dashboard_view, name='dashboard'),

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

    
    # Curriculum paths
    path('cards/deck_list/', curriculum_view, name='deck_list'),
    path('deck/<int:deck_id>/add-to-curriculum/', add_to_curriculum, name='add-to-curriculum'),
    path('deck/<int:deck_id>/remove-from-curriculum/', remove_from_curriculum, name='remove-from-curriculum'),
    path('curriculum/', curriculum_view_modify, name='user_deck_list'), 

    # Card paths
    path('card-list', CardListView.as_view(), name="card-list"),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('decks/<str:subject>/<int:id>/previous/', PreviousCardView.as_view(), name='previous-card'),
    path('decks/<str:subject>/<int:id>/next/', NextCardView.as_view(), name='next-card'),

    # Study and Review paths
    path('study_session/<int:card_id>/', study_session, name='study_session'),

    # Upload paths (staff only)
    path('deck/<int:deck_id>/upload/', upload_cards, name='upload-cards'),
    path('upload/', user_passes_test(staff_check)(upload_cards), name='upload-cards'),
    
    path('progress-log/', user_progress_log, name='user_progress_log'),
    path('cards-in-box/<int:box_level>/', cards_in_box, name='cards_in_box'),


]
