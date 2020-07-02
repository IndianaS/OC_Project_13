from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from figurines.models import DidYouSee



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class CustomCommentCreationForm(ModelForm):
    title = forms.CharField(label="Titre")
    #text = forms.TextField(label="Texte")
    class Meta:
        model = DidYouSee
        fields = ("title", "text", "date")
