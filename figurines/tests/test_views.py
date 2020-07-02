from django.test import TestCase


class FigurineTestViews(TestCase):

    def test_figurine_add_figurine(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post("/figurines/add_figurine/",
                                    {
                                        "id": "31",
                                        "category": "World of Warcraft",
                                        "name": "Thrall"
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('figurines/collection.html')
    
    def test_figurine_collection_user(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get('/figurines/collection/?q=logan')
        self.assertEqual(response.status_code, 302)

    def test_figurine_search(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get('/figurines/collection/?q=logan')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('figurines/collection.html')
