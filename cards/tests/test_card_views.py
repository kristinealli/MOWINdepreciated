import json
import pytest
from django.urls import reverse
from cards.models import Deck, Card



@pytest.mark.django_db
def test_card_detail_view(client, authenticated_user, sample_card):
    client.force_login(authenticated_user)
    url = reverse('card-detail', args=[sample_card.pk])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['object'] == sample_card
    assert 'previous_card' in response.context
    assert 'next_card' in response.context


@pytest.mark.django_db
def test_upload_cards_success(client, admin_user):
    client.force_login(admin_user)
    url = reverse('upload-cards')
    valid_json = {
        "name": "Test Deck",
        "description": "This is a test deck.",
        "is_public": True,
        "cards": [
            {"english": "Hello", "anishinaabemowin": "Aanii", "pronunciation": "Ah-nee"},
            {"english": "Thank you", "anishinaabemowin": "Miigwech"}
        ]
    }

    response = client.post(url, {"json_data": json.dumps(valid_json)})
    assert response.status_code == 302  # Redirect to deck-list
    assert Deck.objects.filter(name="Test Deck").exists()
    assert Card.objects.filter(english="Hello", anishinaabemowin="Aanii").exists()


@pytest.mark.django_db
def test_upload_cards_invalid_json(client, admin_user):
    client.force_login(admin_user)
    url = reverse('upload-cards')
    invalid_json = '{"name": "Test Deck", "cards": [invalid]}'

    response = client.post(url, {"json_data": invalid_json})
    assert response.status_code == 200  # Form re-renders with an error
    assert "Invalid JSON format" in response.content.decode()


@pytest.mark.django_db
def test_upload_cards_missing_fields(client, admin_user):
    client.force_login(admin_user)
    url = reverse('upload-cards')
    json_with_missing_fields = {
        "name": "Incomplete Deck",
        "cards": [{"anishinaabemowin": "Aanii"}]
    }

    response = client.post(url, {"json_data": json.dumps(json_with_missing_fields)})
    assert response.status_code == 302  # Redirect to upload-cards
    assert "Card skipped" in response.cookies["messages"].value  # Check messages middleware


@pytest.mark.django_db
def test_upload_cards_permission_denied(client, authenticated_user):
    client.force_login(authenticated_user)  # Non-admin user
    url = reverse('upload-cards')

    response = client.get(url)
    assert response.status_code == 403  # Permission Denied
