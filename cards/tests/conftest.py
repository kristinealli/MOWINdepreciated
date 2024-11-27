import pytest

from django.contrib.auth import get_user_model
from cards.models import Deck, Card, UserDeck, UserCardProgress

User = get_user_model()

@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(username='testuser', password='password')
    return user

@pytest.fixture
def sample_deck():
    return Deck.objects.create(name="Sample Deck", description="A sample flashcard deck.")

@pytest.fixture
def sample_card(sample_deck):
    return Card.objects.create(
        deck=sample_deck,
        english="Hello",
        anishinaabemowin="Aanii",
        pronunciation="ah-nee",
    )

@pytest.fixture
def sample_user_deck(authenticated_user, sample_deck):
    user_deck = UserDeck.objects.create(profile=authenticated_user.profile)
    user_deck.cards.set(sample_deck.cards.all())
    return user_deck
