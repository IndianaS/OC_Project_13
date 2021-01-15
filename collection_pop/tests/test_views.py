  
from django.test import TestCase


class CollectionPopTestViews(TestCase):
    def test_views_collection_pop_home(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("collection_pop/home.html")

    def test_views_collection_pop_legal_notice(self):
        response = self.client.get("/legal_notice/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("collection_pop/legal_notice.html")

    def test_views_collection_pop_contact_us(self):
        response = self.client.get("/contact_us/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("collection_pop/contact_us.html")

    def test_views_collection_pop_who_are_we(self):
        response = self.client.get("/who_are_we/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("collection_pop/who_are_we.html")
