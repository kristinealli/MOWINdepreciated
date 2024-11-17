from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card, Profile, Deck

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'anishinaabemowin',
            'english',
            'pronunciation',
            'subject'
        ]
        widgets = {
            'anishinaabemowin': forms.TextInput(attrs={'class': 'form-control'}),
            'english': forms.TextInput(attrs={'class': 'form-control'}),
            'pronunciation': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProfileForm(forms.ModelForm):
    decks_in_curriculum = forms.ModelMultipleChoiceField(
        queryset=Deck.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
            'multiple': True
        }),
        label="Select Your Decks",
        required=False
    )

    class Meta:
        model = Profile
        fields = [
            'preferred_name',
            'decks_in_curriculum'
        ]
        widgets = {
            'preferred_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your preferred name'
            }),
        }

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label='Select a CSV file',
        help_text='Max. 42 megabytes',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            if not file.name.endswith('.csv'):
                raise forms.ValidationError('File must be a CSV')
            if file.size > 42 * 1024 * 1024:  # 42MB limit
                raise forms.ValidationError('File size must be under 42MB')
        return file

class CustomUserCreationForm(UserCreationForm):
    preferred_name = forms.CharField(
        label='Preferred Name',
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'What should we call you?'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'preferred_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

        