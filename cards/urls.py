# from django.urls import path
# #from django.views.generic import TemplateView
# from . import views


# urlpatterns = [
#     path(
#         "",
#         views.CardListView.as_view(),
#         name="card-list",
#     ),
#     path(
#         "new",
#         views.CardCreateView.as_view(),
#         name="card-create"
#     ),
# ]


from django.urls import path
from .views import CardListView, CardCreateView, CardUpdateView, BoxView, PreviousCardView, NextCardView, AboutView, DeckListView, DeckDetailView, DeckCreateView, CardUploadView, CardDeleteView, DeckDeleteView

urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path("new", CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
    path('card-check/', BoxView.as_view(), name='card-check'),
    path('card/<int:pk>/previous/', PreviousCardView.as_view(), name='previous-card'),
    path('card/<int:pk>/next/', NextCardView.as_view(), name='next-card'),
    path('about/', AboutView.as_view(), name='about'),
    path('decks/', DeckListView.as_view(), name='deck-list'),  
    path('decks/<str:subject>/', DeckDetailView.as_view(), name='deck-detail'),  
    path('decks/add/', DeckCreateView.as_view(), name='deck-create'),  
    path('cards/upload/', CardUploadView.as_view(), name='cards-upload'), 
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),
    path('decks/<str:subject>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    path('decks/<str:subject>/add-card/', CardCreateView.as_view(), name='card-create'),

]  
