from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nom d'utilisateur *"
            }))
    
    email = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'placeholder': "Adresse mail *"
            }))
    
    password1 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Mot de passe *"
            }))

    password2 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirmation du mot de passe *"
            }))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
