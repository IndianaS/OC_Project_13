from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse
from figurines.views import add_figurine, collection_user, did_you_see, search


class FigurineTestUrls(TestCase):

    def test_figurine_url_add_figurine_view(self):
        found = resolve(reverse("figurines:add_figurine"))
        self.assertEqual(found.func, add_figurine)

    def test_figurine_url_collection_figurine_view(self):
        found = resolve(reverse("figurines:collection"))
        self.assertEqual(found.func, collection_user)
    
    def test_figurine_url_did_you_see_view(self):
        found = resolve(reverse("figurines:did_you_see"))
        self.assertEqual(found.func, did_you_see)

    def test_figurine_url_search_view(self):
        found = resolve(reverse("figurines:search"))
        self.assertEqual(found.func, search)