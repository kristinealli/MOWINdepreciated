import os
import django

import json
from cards.models import Card, Deck


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace 'your_project' with your project name
django.setup()


# Path to your JSON file
# RUN: python manage.py shell < load_cards.py
JSON_FILE_PATH = 'cards.json'

def load_cards_from_json(file_path):
    """
    Load cards and their associated decks from a JSON file into the database.

    Args:
        file_path (str): Path to the JSON file containing deck and card data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for deck_data in data:
        deck, created = Deck.objects.get_or_create(
            name=deck_data['name'],
            defaults={'description': deck_data['description'], 'is_public': deck_data['is_public']}
        )
        if created:
            print(f"Created new deck: {deck.name}")
        else:
            print(f"Deck already exists: {deck.name}")

        # Add cards to the deck
        for card_data in deck_data['cards']:
            card, card_created = Card.objects.get_or_create(
                anishinaabemowin=card_data['anishinaabemowin'],
                english=card_data['english'],
                pronunciation=card_data.get('pronunciation', ''),
                subject=deck.name,  
                deck=deck
            )
            if card_created:
                print(f"Added card: {card.anishinaabemowin} - {card.english}")
            else:
                print(f"Card already exists: {card.anishinaabemowin} - {card.english}")

if __name__ == '__main__':
    print("Loading cards from JSON...")
    load_cards_from_json(JSON_FILE_PATH)
    print("Finished loading cards.")
