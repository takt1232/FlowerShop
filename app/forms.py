from django import forms
from .models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Flower Name'}),
            'category': forms.Select(attrs={'class': 'form-select'})  # ← dropdown styling
        }
