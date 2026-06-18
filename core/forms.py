from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'facebook_url', 'twitter_url', 'pinterest_url', 'dribbble_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about yourself...'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook Profile URL'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter Profile URL'}),
            'pinterest_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Pinterest Profile URL'}),
            'dribbble_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Dribbble Profile URL'}),
        }
