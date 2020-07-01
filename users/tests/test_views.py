from django.test import TestCase

from users.models import User


class UsersTestViews(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="UserTest", password="PaswordOfTheTest&120")
    
    def test_user_profile(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get("/users/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("users/profile.html")
    
    def test_user_create_account_successfully(self):
        response = self.client.post("/users/create_account/",
                                    {
                                        "username": "TestUser",
                                        "password1": "PaswordOfTheTest&120",
                                        "password2": "PaswordOfTheTest&120"
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/profile.html')
    
    def test_user_add_figurine(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post("/users/add_figurine/",
                                    {
                                        "id": "31",
                                        "category": "World of Warcraft",
                                        "name": "Thrall"
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/collection.html')

    def test_user_collection_user(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get('/users/collection/?q=logan')
        self.assertEqual(response.status_code, 200)

    def test_user_did_you_see(self):
        pass
