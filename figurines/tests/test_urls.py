from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse
from figurines.views import add_figurine


class FigurineTestUrls(TestCase):

    def test_figurine_url_add_figurine_view(self):
        found = resolve(reverse("figurines:add_figurine"))
        self.assertEqual(found.func, add_figurine)
