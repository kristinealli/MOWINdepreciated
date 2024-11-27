from django.urls import reverse
import pytest
from cards.models import UserDeck, Deck

@pytest.mark.django_db
def test_add_to_curriculum(client, authenticated_user, sample_deck):
    client.force_login(authenticated_user)
    url = reverse('add_to_curriculum', args=[sample_deck.id])
    response = client.post(url)

    assert response.status_code == 302  # Redirect after POST
    assert sample_deck in authenticated_user.profile.chosen_decks.all()
    assert UserDeck.objects.filter(profile=authenticated_user.profile).exists()
