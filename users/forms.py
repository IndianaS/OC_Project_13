from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from figurines.models import Figurine, DidYouSee, Category



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class CustomAddFigurineCreationForm(ModelForm):
    name = forms.CharField(label="Nom de la figurine")
    picture_figurine = forms.ImageField(label="Photo de la figurine")
    id = forms.IntegerField(label="Numéro de la figurine")
    category = forms.CharField(label="Categorie de la figurine")
    picture_figurine = forms.ImageField(label="Image", required = False)

    class Meta:
        model = Figurine
        fields = ("id", "category", "name", "picture_figurine")

    def clean(self, commit=True):
        category_name = self.cleaned_data.get('category')
        try:
            category = Category.objects.get(name__iexact=category_name)
        except Category.DoesNotExist:
            category = Category.objects.create(name=category_name)

        self.cleaned_data['category'] = category
        return super(CustomAddFigurineCreationForm, self).clean()


class CustomCommentCreationForm(ModelForm):
    title = forms.CharField(label="Titre")
    #text = forms.TextField(label="Texte")
    class Meta:
        model = DidYouSee
        fields = ("title", "text", "date")
