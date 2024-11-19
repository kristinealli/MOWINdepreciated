from django.db import models

class Card(models.Model):
    """
    Represents a single flashcard with Anishinaabemowin and English translations.

    Attributes:
        anishinaabemowin (str): The Anishinaabemowin word or phrase
        english (str): The English translation
        subject (str): The category or subject area of the card
        date_created (datetime): When the card was created
    """
    objects = models.Manager()
    anishinaabemowin = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deck = models.ForeignKey(
        'cards.Deck',
        on_delete=models.CASCADE,
        related_name='cards'
    )
    example_sentence = models.TextField(blank=True) #Next Phase
    audio_file = models.FileField(upload_to='card_audio/', blank=True) #Next Phase
    
    def __str__(self) -> str:
        return f"{self.anishinaabemowin} - {self.english}"
    
    @property
    def get_subject(self):
        """Returns the subject if it exists, otherwise returns the deck name"""
        return self.subject or self.deck.name
    
export_models = [Card]

