import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from flashcards.cards.models import Card, Deck


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'seed_data.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for deck_data in data:
            deck = Deck.objects.create(
                name=deck_data['name'],
                description=deck_data['description'],
                is_public=deck_data['is_public']
            )
            
            for card_data in deck_data['cards']:
                Card.objects.create(
                    deck=deck,
                    anishinaabemowin=card_data['anishinaabemowin'],
                    english=card_data['english'],
                    pronunciation=card_data['pronunciation']
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))