from django.db import models

# Create your models here.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    anishinaabemowin = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.anishinaabemowin} - {self.english}"  # Adjust this to the fields you want to display

