from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse

from django.contrib.auth.views import LoginView
from users.views import profile, create_account


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
