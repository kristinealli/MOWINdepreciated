from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    AboutView,
    BoxView,
    CardCreateView,
    CardDeleteView,
    CardDetailView,
    CardListView,
    CardUpdateView,
    CardUploadView,
    DeckCreateView,
    DeckDeleteView,
    DeckDetailView,
    DeckListView,
    NextCardView,
    PreviousCardView,
    ProfileCreateView,
    ProfileDetailView,
    ProfileUpdateView,
    signup,
    study_session,
    upload_cards,
    dashboard,
    home,
    review_card,
    profile_setup,
    add_to_curriculum, 
    remove_from_curriculum,
    UserDeckListView, 
    deck_stats,
    curriculum_view, 
    CardsInDeckView, 
)


urlpatterns = [
    # General paths
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),

    # Deck-related paths
    path('decks/', DeckListView.as_view(), name='deck-list'),
    path('decks/add/', DeckCreateView.as_view(), name='deck-create'),
    path('decks/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/<str:subject>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    path('decks/<str:subject>/add-card/', CardCreateView.as_view(), name='card-create'),
    path('deck/<int:pk>/add-to-curriculum/', add_to_curriculum, name='add-to-curriculum'),
    path('deck/<int:pk>/remove-from-curriculum/', remove_from_curriculum, name='remove-from-curriculum'),
    path('deck/<int:pk>/cards/', CardsInDeckView.as_view(), name='cards-in-deck'),

    # Card-related paths
    path("new", CardCreateView.as_view(), name="card-create"),
    path("card-list", CardListView.as_view(), name="card-list"),
    path("edit/<int:pk>", CardUpdateView.as_view(), name="card-update"),
    path('cards/upload/', CardUploadView.as_view(), name='cards-upload'),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),

    # Learning/Review paths
    path('decks/<str:subject>/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('decks/<str:subject>/<int:pk>/previous/', PreviousCardView.as_view(), name='previous-card'),
    path('decks/<str:subject>/<int:pk>/next/', NextCardView.as_view(), name='next-card'),
    path('deck/<int:pk>/stats/', deck_stats, name='deck-stats'),

    # Study URLs
    path('deck/<int:deck_pk>/study/', study_session, name='study_session'),
    path('deck/<int:deck_pk>/upload/', upload_cards, name='upload-cards'),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
    path('card-check/', BoxView.as_view(), name='card-check'),

    # Login/Logout and User paths
    path('login/', auth_views.LoginView.as_view(template_name='cards/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/setup/', profile_setup, name='profile-setup'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('dashboard/', dashboard, name='dashboard'),

    # Review paths
    path('deck/<int:deck_id>/review/<int:card_id>/', review_card, name='review-card'),
    path('curriculum/', UserDeckListView.as_view(), name='user-deck-list'),
    path('curriculum/', curriculum_view, name='curriculum'),
    path('deck/<int:pk>/add-to-curriculum/', add_to_curriculum, name='add-to-curriculum'),
    path('deck/<int:pk>/remove-from-curriculum/', remove_from_curriculum, name='remove-from-curriculum'),

]
