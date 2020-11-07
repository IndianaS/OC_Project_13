from django.test import TestCase
from django.urls import reverse

from users.models import User
from friendship.models import Friend, FriendshipRequest


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

    def test_user_create_account_view(self):
        response = self.client.get("/users/create_account/")
        self.assertEqual(response.status_code, 200)

    def test_user_create_account_successfully(self):
        response = self.client.post(
            "/users/create_account/",
            {
                "username": "NewTestUser",
                "email": "newtestuser@mail.com",
                "password1": "PaswordOfTheTest&120",
                "password2": "PaswordOfTheTest&120",
            },
        )

        new_user = User.objects.filter(username="NewTestUser").first()

        self.assertEqual(new_user.username, "NewTestUser")
        self.assertEqual(response.status_code, 302)
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

    def test_user_del_existing_user(self):
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
        self.client.login(username="UserForAddFriend",
                          password="PaswordTest&120")
        current_user = User.objects.get(username="UserForAddFriend")
        other_user = User.objects.get(username='UserTest')
        add_friend = Friend.objects.add_friend(other_user, current_user)

        response = self.client.post(
            "/users/accept_request/",
            {
                "other_user_id": other_user.id,
                "user_choice": "Accepted",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/friends_list.html')

    def test_user_reject_request(self):
        self.client.login(username="UserForAddFriend",
                          password="PaswordTest&120")

        current_user = User.objects.get(username="UserForAddFriend")
        other_user = User.objects.get(username='UserTest')
        add_friend = Friend.objects.add_friend(other_user, current_user)

        response = self.client.post(
            "/users/accept_request/",
            {
                "other_user_id": other_user.id,
                "user_choice": "Reject",
            },
        )

        try:
            friend_request = FriendshipRequest.objects.get(
                from_user=other_user.id, to_user=current_user.id
            )
        except FriendshipRequest.DoesNotExist:
            friend_request = None

        self.assertEqual(friend_request, None)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/friends_list.html')

    def test_user_remove_friend(self):
        pass

    """
    def test_user_friends_figurine(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get("/users/friends_figurine/1")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/friends_figurine.html')
    
    def test_user_friends_figurine_search(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get(
            "/users/friends_figurine_search/?q=Logan&friend_id=1"
            )

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/friends_figurine_search.html')
    """