from django.test import TestCase
from django.urls import reverse

from users.models import User


class UsersTestViews(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="UserTest", password="PaswordOfTheTest&120"
        )
        User.objects.create_user(
            username="UserForAddFriend", password="PaswordTest&120"
        )

    def test_user_profile(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get("/users/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("users/profile.html")

    def test_user_create_account_successfully(self):
        response = self.client.post(
            "/users/create_account/",
            {
                "username": "TestUser",
                "password1": "PaswordOfTheTest&120",
                "password2": "PaswordOfTheTest&120",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/profile.html')

    def test_user_create_account_invalid(self):
        response = self.client.post(
            "/users/create_account/",
            {
                "username": "TestUser",
                "password1": "PaswordOfTheTest&120",
                "password2": "PaswordTest&120",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/create_account.html')

    def test_user_del_user(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get(
            reverse('users:del_user')
            )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('/')

    def test_user_friends_list(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get("/users/friends_list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("users/friends_list.html")

    def test_user_add_friend(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post(
            "/users/add_friend/",
            {
                "username": "UserForAddFriend",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/friends_list.html')

    def test_user_accept_request(self):
        self.client.login(username="UserForAddFriend", password="PaswordTest&120")
        response = self.client.post(
            "/users/friends_list/",
            {
                "username": "UserTest",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/friends_list.html')

    def test_user_remove_friend(self):
       pass
