from django.test import TestCase
from django.urls import reverse

from accounts.signals import User


class TestUserProfileView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_user_profile_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)

    def test_user_profile_namespace(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("user_profile"))
        self.assertEqual(response.status_code, 200)
