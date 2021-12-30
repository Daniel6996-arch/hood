from django import forms
from .models import NeighbourHood, Business

class HoodForm(forms.ModelForm): 

    class Meta:
        model = NeighbourHood
        exclude = ['admin', 'uploaded_on']
