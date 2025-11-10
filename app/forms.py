from django import forms
from .models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Flower Name'}),
        }
        