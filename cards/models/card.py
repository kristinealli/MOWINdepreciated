from django.db import models

class Card(models.Model):
    """
    Represents a single flashcard with Anishinaabemowin and English translations.

    Attributes:
        anishinaabemowin (str): The Anishinaabemowin word or phrase.
        english (str): The English translation.
        pronunciation (str): Pronunciation of the Anishinaabemowin word.
        subject (str): The category or subject area of the card.
        date_created (datetime): When the card was created.
        date_modified (datetime): When the card was last modified.
        deck (ForeignKey): The deck the card belongs to.
        example_sentence (TextField): Example sentence using the Anishinaabemowin word.(Next Phase)
        audio_file (FileField): Audio file for the card. (Next Phase)
        image_file (ImageField): Image file for the card. (Next Phase)
    """
    
    objects = models.Manager()
    anishinaabemowin = models.CharField(max_length=100, unique=True, help_text="The Anishinaabemowin word or phrase")
    english = models.CharField(max_length=100, unique=True, help_text="The English translation")
    pronunciation = models.CharField(max_length=100, blank=True, help_text="Pronunciation of the Anishinaabemowin word")
    subject = models.CharField(max_length=100, blank=True, null=True, help_text="The category or subject area of the card")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)  
    deck = models.ForeignKey(
        'Deck',
        on_delete=models.CASCADE,
        related_name='cards'
    )
    example_sentence = models.TextField(blank=True, help_text="Example sentence using the Anishinaabemowin word")  # Next Phase
    audio_file = models.FileField(upload_to='card_audio/', blank=True, help_text="Audio file for the card")  # Next Phase
    image_file = models.ImageField(upload_to='card_images/', blank=True, help_text="Image file for the card")  # Next Phase 
    
    def __str__(self) -> str:
        return f"{self.anishinaabemowin} - {self.english}"
    
    @property
    def get_subject(self):
        """Returns the subject if it exists, otherwise returns the deck name"""
        return self.subject or self.deck.name

    class Meta:
        verbose_name = "Flashcard"
        verbose_name_plural = "Flashcards"

