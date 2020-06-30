from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from figurines.models import Figurine



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class CustomAddFigurineCreationForm(ModelForm):
    name = forms.CharField(label="Nom de la figurine")
    picture_figurine = forms.ImageField(label="Photo de la figurine")
    id = forms.IntegerField(label="Numéro de la figurine")
    id_category = forms.IntegerField(label="Categorie de la figurine")
    class Meta:
        model = Figurine
        name = forms.CharField(label="Nom de la figurine")
        fields = ("id", "id_category", "name", "picture_figurine")



class CustomReadBddCreationForm():
    class Meta:
        pass