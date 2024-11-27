from django.urls import reverse
import pytest
from cards.models import UserCardProgress, UserDeck

@pytest.mark.django_db
def test_study_session(client, authenticated_user, sample_user_deck):
    client.force_login(authenticated_user)
    url = reverse('study_session', args=[sample_user_deck.id])
    response = client.get(url)

    assert response.status_code == 200
    assert 'due_cards' in response.context
    assert 'current_card' in response.context
    assert response.context['cards_due'] == sample_user_deck.get_due_cards().count()
