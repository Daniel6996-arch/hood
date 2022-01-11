from django import forms
from django.contrib.auth.models import User
from .models import NeighbourHood, Business, Posts

class HoodForm(forms.ModelForm): 

    class Meta:
        model = NeighbourHood
        exclude = ['admin', 'uploaded_on']

class BusinessForm(forms.ModelForm): 

    class Meta:
        model = Business
        exclude = ['hood','business_user', 'uploaded_on']

class PostForm(forms.ModelForm): 

    class Meta:
        model = Posts
        exclude = ['author', 'created_on'] 

class UserForm(forms.ModelForm):

    class Meta:
        model = User 
        exclude = ['full_name']              