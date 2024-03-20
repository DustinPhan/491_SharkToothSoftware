# forms.py

from django import forms
from .models import Person

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'arm']  # Define fields you want to include in the form