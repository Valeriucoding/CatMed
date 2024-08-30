from django.urls import reverse

from catalog.models import Organ
from catalog.tests.factories import CatalogFactory


class TestOrganModel(CatalogFactory):
    def test_create_organ(self):
        self.assertEqual(str(self.organ), "Head")

    def test_update_organ(self):
        self.organ.name = "Brain"
        self.organ.save()
        self.assertEqual(str(self.organ), "Brain")

    def test_delete_organ(self):
        self.organ.delete()
        self.assertEqual(Organ.objects.count(), 0)


class TestOrganViews(CatalogFactory):
    def test_organ_list_url(self):
        response = self.client.get("/organs/")
        self.assertEqual(response.status_code, 200)

    def test_organ_list_namespace(self):
        url = reverse("catalog:organ_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_organ_create_url(self):
        response = self.client.get("/organs/create/")
        self.assertEqual(response.status_code, 200)

    def test_organ_create_namespace(self):
        url = reverse("catalog:organ_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_organ_list_create_url(self):
        response = self.client.get("/organs/create-table-item")
        self.assertEqual(response.status_code, 200)

    def test_organ_list_create_namespace(self):
        url = reverse("catalog:organ_list_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_organ_edit_url(self):
        response = self.client.get("/organs/edit/1/")
        self.assertEqual(response.status_code, 200)

    def test_organ_edit_namespace(self):
        url = reverse("catalog:organ_edit", kwargs={"organ_id": self.organ.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
