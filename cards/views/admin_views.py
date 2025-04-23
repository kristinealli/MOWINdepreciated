# Django imports
import json
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import redirect, render
from cards.models import Deck, Card


class CardUploadForm(forms.Form):
    json_data = forms.JSONField()
    
@login_required
def upload_cards(request):
    if not request.user.is_staff and not request.user.is_superuser:
        raise PermissionDenied("You don't have permission to upload cards.")

    if request.method == 'POST':
        try:
            # Retrieve and parse JSON data
            json_data = request.POST.get('json_data')
            if not json_data:
                messages.error(request, "Please provide JSON data.")
                return redirect('upload-cards')

            data = json.loads(json_data)

            # Validate required deck fields
            deck_name = data.get('name')
            if not deck_name:
                messages.error(request, "The 'name' field is required for the deck.")
                return redirect('upload-cards')

            # Create or get the deck
            deck, created = Deck.objects.get_or_create(
                name=deck_name,
                defaults={
                    'description': data.get('description', ''),
                    'is_public': data.get('is_public', True),
                }
            )

            # Validate and create cards
            cards_data = data.get('cards', [])
            if not cards_data:
                messages.error(request, "No cards found in the provided JSON.")
                return redirect('upload-cards')

            cards_created = 0
            for card_data in cards_data:
                try:
                    # Ensure required fields are present
                    english = card_data.get('english')
                    anishinaabemowin = card_data.get('anishinaabemowin')
                    if not english or not anishinaabemowin:
                        messages.warning(
                            request, "Card skipped: 'english' and 'anishinaabemowin' are required fields."
                        )
                        continue

                    # Create or update the card
                    card, created = Card.objects.get_or_create(
                        deck=deck,
                        english=english,
                        defaults={
                            'anishinaabemowin': anishinaabemowin,
                            'pronunciation': card_data.get('pronunciation', ''),
                            'subject': card_data.get('subject', ''),
                            'example_sentence': card_data.get('example_sentence', ''),
                            'audio_file': card_data.get('audio_file', None),
                            'image_file': card_data.get('image_file', None),
                        }
                    )
                    if created:
                        cards_created += 1
                    else:
                        # Update card fields if needed
                        updated = False
                        for field in ['anishinaabemowin', 'pronunciation', 'subject', 'example_sentence']:
                            new_value = card_data.get(field, getattr(card, field))
                            if getattr(card, field) != new_value:
                                setattr(card, field, new_value)
                                updated = True

                        if updated:
                            card.save()
                            messages.info(
                                request, f"Updated existing card with English '{english}'."
                            )
                except IntegrityError:
                    messages.error(
                        request, f"Failed to process card with English '{card_data.get('english')}'."
                    )
                except Exception as e:
                    messages.error(request, f"Unexpected error: {str(e)}")            
            
            if cards_created > 0:
                messages.success(
                    request,
                    f'Successfully created {cards_created} cards in deck "{deck.name}"!'
                )
            else:
                messages.warning(request, "No valid cards were created.")

            return redirect('deck-list')

        except json.JSONDecodeError as e:
            messages.error(request, f'Invalid JSON format: {str(e)}')

    return render(request, 'cards/upload.html')
