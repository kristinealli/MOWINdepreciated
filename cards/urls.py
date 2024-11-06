from django.urls import path
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
)


urlpatterns = [
    # General paths
    path('about/', AboutView.as_view(), name='about'),
    path("", CardListView.as_view(), name="card-list"),

    # Deck-related paths
    path('decks/', DeckListView.as_view(), name='deck-list'),  
    path('decks/add/', DeckCreateView.as_view(), name='deck-create'),  
    path('decks/<str:subject>/', DeckDetailView.as_view(), name='deck-detail'),  
    path('decks/<str:subject>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    path('decks/<str:subject>/add-card/', CardCreateView.as_view(), name='card-create'),

    # Card-related paths
    path("new", CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", CardUpdateView.as_view(), name="card-update"),
    path('cards/upload/', CardUploadView.as_view(), name='cards-upload'),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),

    # Learning/Review paths
    path('decks/<str:subject>/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('decks/<str:subject>/<int:pk>/previous/', PreviousCardView.as_view(), name='previous-card'),
    path('decks/<str:subject>/<int:pk>/next/', NextCardView.as_view(), name='next-card'),
    
    # Box-related paths
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
    path('card-check/', BoxView.as_view(), name='card-check'),
]

