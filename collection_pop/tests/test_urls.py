from collection_pop.views import home
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve


class UrlTestCase(TestCase):

    def test_home_url_view(self):
        found = resolve(reverse("home"))
        self.assertEqual(found.func, home)
