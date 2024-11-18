from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from django.utils import timezone
from .models import UserCardProgress, Deck, Card

class DashboardTests(TestCase):
    """Test suite for the dashboard functionality.
    
    Tests dashboard views, caching behavior, and statistics calculations
    for user card progress and deck management.
    """

    def setUp(self):
        """Set up test data.
        
        Creates:
            - A test user with associated profile
            - A test deck associated with the user
            - 25 test cards (5 cards in each of the 5 Leitner boxes)
        """
        # Create test user
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Get the automatically created profile
        self.profile = self.user.profile
        
        self.client.login(username='testuser', password='testpass123')
        
        # Create test deck
        self.deck = Deck.objects.create(
            name='Test Deck',
            owner=self.user
        )
        self.profile.chosen_decks.add(self.deck)
        
        # Create cards in different boxes
        self.create_test_cards()

    def create_test_cards(self):
        """Create test cards distributed across Leitner boxes.
        
        Creates 5 cards in each box level (1-5) with successful review history.
        Each card is created with matching English and Anishinaabemowin text
        and associated UserCardProgress record.
        """
        now = timezone.now()
        # Create 5 cards in each box level
        for box in range(1, 6):  # Boxes 1-5
            for i in range(5):
                card = Card.objects.create(
                    deck=self.deck,
                    english=f'test_{box}_{i}',
                    anishinaabemowin=f'test_{box}_{i}'
                )
                UserCardProgress.objects.create(
                    user=self.user,
                    card=card,
                    box_level=box,
                    last_reviewed=now,
                    next_review_date=now,
                    last_review_result=True  # Set all reviews as correct
                )

    def test_dashboard_caching(self):
        """Verify dashboard data caching functionality.
        
        Tests that:
            - Initial request populates the cache
            - Cache contains correct data
            - Total due cards count is accurate
        """
        cache.clear()
        
        # First request - should hit database
        response1 = self.client.get(reverse('dashboard'))
        self.assertEqual(response1.status_code, 200)
        
        # Get cached data
        cache_key = f'user_dashboard_{self.user.id}'
        cached_data = cache.get(cache_key)
        self.assertIsNotNone(cached_data)
        
        # Verify total due cards (all cards are due in our test setup)
        self.assertEqual(cached_data['total_due_cards'], 25)

    def test_deck_statistics(self):
        """Verify deck statistics calculations.
        
        Tests that:
            - Total card count is correct
            - Box distribution counts are accurate
        """
        response = self.client.get(reverse('dashboard'))
        deck_stats = response.context['user_decks'][0]
        
        # Test deck statistics
        self.assertEqual(deck_stats['total_cards'], 25)  # 5 cards in each box
        self.assertEqual(
            deck_stats['box_distribution'][5]['count'], 
            5
        )  # 5 cards in box 5

    def test_today_statistics(self):
        """Verify today's study statistics calculations.
        
        Tests that:
            - Review count for today is accurate
            - Study accuracy percentage is correct
        """
        response = self.client.get(reverse('dashboard'))
        
        # Test today's statistics
        self.assertEqual(response.context['today_reviews_count'], 25)
        self.assertEqual(response.context['today_accuracy'], 100)

    def test_dashboard_load(self):
        """Verify basic dashboard page loading.
        
        Tests that:
            - Dashboard page returns 200 status code
            - Correct template is used
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/dashboard.html')
