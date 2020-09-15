from django.test import TestCase


class CollectionPopTestViews(TestCase):
    def test_views_collection_pop_home(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
