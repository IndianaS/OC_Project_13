from django.test import TestCase

from figurines.forms import CustomAddFigurineCreationForm


class FgurinesFormTestCase(TestCase):

    def test_figurine_custom_form_add_figurine_is_valid(self):
        form = CustomAddFigurineCreationForm(data={
           "figurine_number": 31,
           "category": "World of Warcraft",
           "name": "Thrall"
            })
        self.assertTrue(form.is_valid())

    def test_figurine_custom_form_add_figurine_is_not_valid(self):
        form = CustomAddFigurineCreationForm(data={
           "figurine_number": 31,
           "category": "World of Warcraft",
           "name": ""
            })
        self.assertFalse(form.is_valid())
