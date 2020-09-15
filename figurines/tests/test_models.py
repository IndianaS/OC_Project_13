from django.test import TestCase

from figurines.models import Category, DidYouSee, Figurine
from users.models import User


class FigurineTestsModels(TestCase):
    def test_models_category_figurine(self):
        category = Category.objects.create(name="world of warcraft")
        self.assertEquals(category.name, "world of warcraft")

    def test_models_figurine(self):
        category = Category.objects.create(name="world of warcraft")
        figurine = Figurine.objects.create(
            figurine_number=31, category=category, name="thrall"
        )
        self.assertEquals(figurine.id, 1)
        self.assertEquals(figurine.category, category)
        self.assertEquals(figurine.name, "thrall")
