from django.test import TestCase


class FigurineTestViews(TestCase):

    def test_user_add_figurine(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post("/users/add_figurine/",
                                    {
                                        "id": "31",
                                        "category": "World of Warcraft",
                                        "name": "Thrall"
                                    })
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('users/collection.html')
    
    def test_user_collection_user(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get('/users/collection/?q=logan')
        self.assertEqual(response.status_code, 404)
