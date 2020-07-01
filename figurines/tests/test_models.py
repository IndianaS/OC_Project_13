from django.test import TestCase
from figurines.models import Category, Collection, DidYouSee, Figurine
from users.models import User


class FigurineTestsModels(TestCase):

    def test_models_category_figurine(self):
        category = Category.objects.create(name="world of warcraft")
        self.assertEquals(category.name, "world of warcraft")
    
    def test_models_figurine(self):
        category = Category.objects.create(name="world of warcraft")
        figurine = Figurine.objects.create(
            id=31,
            category=category,
            name="thrall"
        )
        self.assertEquals(figurine.id, 31)
        self.assertEquals(figurine.category, category)
        self.assertEquals(figurine.name, "thrall")

    def test_models_collection(self):
        category = Category.objects.create(name="wolrd of warcraft")
        figurine = Figurine.objects.create(
            id=31,
            category=category,
            name="thrall"
        )
        user = User.objects.create_user(
            username="UtilisateurTest",
            first_name="utilisateur",
            last_name="Test",
            password="Azertyu&4552"
        )
        Collection.objects.create(
            user=user,
            figurine=figurine
        )
        collection = Collection.objects.all().first()
        self.assertEquals(collection.user, user)
        self.assertEquals(collection.figurine, figurine)
