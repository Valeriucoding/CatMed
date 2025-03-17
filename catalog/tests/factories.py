from django.test import TestCase
from django.contrib.auth.models import User

from catalog.models import Medicine, Disease, MedicationType, Organ


class CatalogFactory(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Create a test user
        cls.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword123"
        )
        
        cls.medicine = Medicine.objects.create(
            name="Paracetamol",
            description="A common painkiller",
        )
        cls.disease = Disease.objects.create(name="Headache")
        cls.medication_type = MedicationType.objects.create(name="Tablet")
        cls.organ = Organ.objects.create(name="Head")
        cls.medicine.diseases.add(cls.disease)
        cls.medicine.medication_types.add(cls.medication_type)

    def login_user(self):
        """Helper method to login the test user for protected endpoints"""
        login_success = self.client.login(
            username="testuser",
            password="testpassword123"
        )
        self.assertTrue(login_success, "Failed to log in test user")
        return login_success
