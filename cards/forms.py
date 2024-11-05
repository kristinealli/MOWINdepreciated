from django import forms
from .models import Card

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)

class FileUploadForm(forms.Form):
    file = forms.FileField(label="Upload Deck", required=True)
    deck_name = forms.CharField(max_length=255, required=True)  
    
class CardForm(forms.ModelForm):
    new_subject = forms.CharField(
        required=False,
        label="Or enter a new deck name",
        widget=forms.TextInput(attrs={"placeholder": "New Deck Name"})
    )

    class Meta:
        model = Card
        fields = ["anishinaabemowin", "english", "subject"]

    def __init__(self, *args, **kwargs):
        current_subject = kwargs.pop('current_subject', None)
        super().__init__(*args, **kwargs)
        
        # Set the dropdown of subjects, with the current subject as the first option
        self.fields["subject"].queryset = Card.objects.values_list('subject', flat=True).distinct()
        self.fields["subject"].initial = current_subject
        self.fields["subject"].required = False

    def clean_subject(self):
        subject = self.cleaned_data.get("subject")
        new_subject = self.cleaned_data.get("new_subject")

        # Use the new subject if provided
        if new_subject:
            return new_subject
        return subject