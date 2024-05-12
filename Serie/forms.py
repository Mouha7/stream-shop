from django import forms
from .models import Serie

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['title', 'description', 'release_date', 'poster', 'number_of_seasons', 'gender']
