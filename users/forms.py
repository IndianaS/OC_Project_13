from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur", 
        widget=forms.TextInput(
            attrs={
                'class': 'test',
                'placeholder': "Nom d'utilisateur *"
            }))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
