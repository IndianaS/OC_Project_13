from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse

from django.contrib.auth.views import LoginView
from users.views import profile, create_account, collection_user, did_you_see


class UrlTestCase(TestCase):

    def test_user_url_login(self):
        found = resolve(reverse("users:login"))
        self.assertEqual(found.func.view_class, LoginView)

    def test_user_url_profile_view(self):
        found = resolve(reverse("users:profile"))
        self.assertEqual(found.func, profile)

    def test_user_url_create_account_view(self):
        found = resolve(reverse("users:create_account"))
        self.assertEqual(found.func, create_account)

    def test_user_url_collection_user_view(self):
        found = resolve(reverse("users:collection"))
        self.assertEqual(found.func, collection_user)
    
    def test_user_url_did_you_see_view(self):
        found = resolve(reverse("users:did_you_see"))
        self.assertEqual(found.func, did_you_see)
