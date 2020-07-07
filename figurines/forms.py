from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from figurines.models import Category, Figurine, DidYouSee


class CustomAddFigurineCreationForm(ModelForm):
    name = forms.CharField(
        label="Nom de la figurine",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom de la figurine *'
            })
    )

    figurine_number = forms.IntegerField(
        label="Numéro de la figurine",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Numéro de la figurine *'
            })
    )

    category = forms.CharField(
        label="Categorie de la figurine",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Catégorie *'
            })
    )

    picture_figurine = forms.ImageField(
        label="Photo de la figurine",
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'input-file'}
        )
    )

    class Meta:
        model = Figurine
        fields = ("figurine_number", "category", "name", "picture_figurine")

    def clean(self, commit=True):
        category_name = self.cleaned_data.get('category')
        try:
            category = Category.objects.get(name__iexact=category_name)
        except Category.DoesNotExist:
            category = Category.objects.create(name=category_name)

        self.cleaned_data['category'] = category
        return super(CustomAddFigurineCreationForm, self).clean()


class CustomCommentCreationForm(ModelForm):
    title = forms.CharField(
        label="Titre",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Titre *'
            }))

    text = forms.CharField(
        label="Titre",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Texte *'
            }))

    class Meta:
        model = DidYouSee
        fields = ("title", "text",)
