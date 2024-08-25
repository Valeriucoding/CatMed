from django.urls import reverse

from catalog.models import MedicationType
from catalog.tests.factories import CatalogFactory


class TestMedicationTypeModel(CatalogFactory):
    def test_create_medication_type(self):
        self.assertEqual(str(self.medication_type), "Tablet")

    def test_update_medication_type(self):
        self.medication_type.name = "Capsule"
        self.medication_type.save()
        self.assertEqual(str(self.medication_type), "Capsule")

    def test_delete_medication_type(self):
        self.medication_type.delete()
        self.assertEqual(MedicationType.objects.count(), 0)


class TestMedicationTypeViews(CatalogFactory):
    def test_medication_type_list_url(self):
        response = self.client.get("/medication-types/")
        self.assertEqual(response.status_code, 200)

    def test_medication_type_list_namespace(self):
        url = reverse("catalog:medication_type_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_medication_type_create_url(self):
        response = self.client.get("/medication_types/create/")
        self.assertEqual(response.status_code, 200)

    def test_medication_type_create_namespace(self):
        url = reverse("catalog:medication_type_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
