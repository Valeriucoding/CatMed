from django.urls import reverse

from catalog.models import Disease
from catalog.tests.factories import CatalogFactory


class TestDiseaseModel(CatalogFactory):
    def test_create_disease(self):
        self.assertEqual(str(self.disease), "Headache")

    def test_update_disease(self):
        self.disease.name = "Migraine"
        self.disease.save()
        self.assertEqual(str(self.disease), "Migraine")

    def test_delete_disease(self):
        self.disease.delete()
        self.assertEqual(Disease.objects.count(), 0)


class TestDiseaseViews(CatalogFactory):
    def test_disease_list_url(self):
        response = self.client.get("/diseases/")
        self.assertEqual(response.status_code, 200)

    def test_disease_list_namespace(self):
        url = reverse("catalog:disease_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_disease_create_url(self):
        response = self.client.get("/disease/create/")
        self.assertEqual(response.status_code, 200)

    def test_disease_create_namespace(self):
        url = reverse("catalog:disease_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_disease_list_create_url(self):
        response = self.client.get("/disease/create-table-item")
        self.assertEqual(response.status_code, 200)

    def test_disease_list_create_namespace(self):
        url = reverse("catalog:disease_list_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_disease_edit_url(self):
        response = self.client.get("/disease/edit/1/")
        self.assertEqual(response.status_code, 200)

    def test_disease_edit_namespace(self):
        url = reverse("catalog:disease_edit", kwargs={"disease_id": self.disease.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
