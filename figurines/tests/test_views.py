from django.test import TestCase
from figurines.models import Figurine, Category, DidYouSee
from users.models import User


class FigurineTestViews(TestCase):
    def setUp(self):
        user_test = User.objects.create_user(
            username="UserTest", password="PaswordOfTheTest&120"
        )
        category_figurine = Category.objects.create(
            name="super heroes"
        )

        figurine = Figurine.objects.create(
            figurine_number="1",
            category=category_figurine,
            name="batman"
        )
        figurine.user.add(user_test)

        return super().setUp()

    def test_figurine_add_figurine(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post(
            "/figurines/add_figurine/",
            {"figurine_number": "31", "category": "World of Warcraft", "name": "Thrall"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('figurines/collection.html')

    def test_figurine_collection_user(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get('/figurines/collection/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/collection.html')

    def test_figurine_search_with_all_figurines(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        user = User.objects.get(username="UserTest")

        response = self.client.get('/figurines/search/?all=all')
        user_figurine = user.figurine_set.all()

        self.assertQuerysetEqual(
            response.context['figurines_list'],
            [repr(figurine) for figurine in user_figurine]
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/search.html')

    def test_figurine_search_without_all_figurines(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        user = User.objects.get(username="UserTest")
        user_figurine = user.figurine_set.all().delete()
    
        response = self.client.get('/figurines/search/?all=all')

        self.assertFalse(response.context['figurines_list'])
        self.assertContains(response, 'Pas de résultat.')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/search.html')

    def test_figurine_search_with_figurines(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        user = User.objects.get(username="UserTest")

        response = self.client.get('/figurines/search/?q=batman')
        user_figurine = user.figurine_set.filter(name__icontains='batman')

        self.assertQuerysetEqual(
            response.context['figurines_list'],
            [repr(figurine) for figurine in user_figurine]
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/search.html')

    def test_figurine_search_without_all_figurines(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        user = User.objects.get(username="UserTest")
        user_figurine = user.figurine_set.filter(name__icontains='batman').delete()
    
        response = self.client.get('/figurines/search/?q=batman')

        self.assertFalse(response.context['figurines_list'])
        self.assertContains(response, 'Pas de résultat.')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/search.html')

    def test_figurine_did_you_see(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.get("/figurines/did_you_see/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("figurines/did_you_see.html")

    def test_create_question(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post(
            "/figurines/create_question",
            {
                "title": "Je recherche batman",
                "text": "Bonjour, je recherche Batman",
                "date": "03/07/2020",
            },
        )
        self.assertRedirects(response, '/figurines/did_you_see/')

        response = self.client.get('/figurines/did_you_see/')

        self.assertContains(response, 'Je recherche batman')
        self.assertTemplateUsed('figurines/did_you_see.html')

    def test_can_respond_to_question(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        response = self.client.post(
            "/figurines/create_question",
            {
                "title": "Je recherche batman2",
                "text": "Bonjour, je recherche Batman2",
                "date": "03/07/2020",
            },
        )
        post = DidYouSee.objects.get(title='Je recherche batman2')

        response_second_message = self.client.post(
            f"/figurines/create_question/{post.id}",
            {
                "title": "J'ai batman2",
                "text": "jai batman",
                "date": "20/07/2020",
            }
        )

        response_detail = self.client.get(f'/figurines/post_detail/{post.id}/')

        self.assertContains(response_detail, "jai batman")
        self.assertTemplateUsed('figurines/post_detail.html')


    def test_post_detail(self):
        self.client.login(username="UserTest", password="PaswordOfTheTest&120")
        user = User.objects.get(username="UserTest")
        post = DidYouSee(
                author=user,
                title="Je recherche batman",
                text="Bonjour, j'ai trouvé Batman",
        )
        post.save()
        post.parent = post
        post.save()
    
        response = self.client.get(
            f"/figurines/post_detail/{post.id}"
        )
        self.assertContains(response, "Je recherche batman")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('figurines/post_detail.html')

    # def test_delete_figurine(self):
    #     self.client.login(username="UserTest", password="PaswordOfTheTest&120")
    #     response = self.client.get('/figurines/collection/?q=logan')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed('figurines/collection.html')

    # def test_report_post(self):
    #     self.client.login(username="UserTest", password="PaswordOfTheTest&120")
    #     response = self.client.post(
    #         "/figurines/post_detail/51/",
    #         {
    #             "title": "Je recherche batman",
    #             "text": "Bonjour, j'ai trouvé Batman",
    #         },
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed('figurines/report_post.html')
