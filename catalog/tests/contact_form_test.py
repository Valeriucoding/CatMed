from django.test import TestCase


class TestContactFormView(TestCase):
    def test_contact_form_view(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_contact_form_namespace(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
