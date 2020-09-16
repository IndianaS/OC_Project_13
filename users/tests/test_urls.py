from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve

from users.views import (accept_request, add_friend, create_account, del_user,
                         friends_figurine, friends_list, profile,
                         remove_friend)


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

    def test_user_url_del_user_view(self):
        found = resolve(reverse("users:del_user"))
        self.assertEqual(found.func, del_user)

    def test_user_url_friends_list_views(self):
        found = resolve(reverse("users:friends_list"))
        self.assertEqual(found.func, friends_list)

    def test_user_url_add_friend_views(self):
        found = resolve(reverse("users:add_friend"))
        self.assertEqual(found.func, add_friend)

    def test_user_url_accept_request_views(self):
        found = resolve(reverse("users:accept_request"))
        self.assertEqual(found.func, accept_request)
    
    def test_user_url_remove_friend_views(self):
        found = resolve(reverse("users:remove_friend"))
        self.assertEqual(found.func, remove_friend)
