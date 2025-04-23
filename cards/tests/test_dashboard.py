import pytest
from django.urls import reverse
from cards.models import UserDeck, UserCardProgress

@pytest.mark.django_db
def test_dashboard_view(client, authenticated_user, sample_user_deck):
    client.force_login(authenticated_user)
    url = reverse('dashboard')
    response = client.get(url)

    assert response.status_code == 200
    assert 'due_cards' in response.context
    assert 'total_box_distribution' in response.context
    assert response.context['count_due_cards'] == sample_user_deck.get_due_cards().count()
