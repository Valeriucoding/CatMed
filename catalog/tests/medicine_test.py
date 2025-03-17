from django.urls import reverse

from catalog.models import Medicine
from catalog.tests.factories import CatalogFactory


class TestMedicineModel(CatalogFactory):
    def test_create_medicine(self):
        self.assertEqual(str(self.medicine), "Paracetamol")

    def test_update_medicine(self):
        self.medicine.name = "Ibuprofen"
        self.medicine.save()
        self.assertEqual(str(self.medicine), "Ibuprofen")

    def test_delete_medicine(self):
        self.medicine.delete()
        self.assertEqual(Medicine.objects.count(), 0)


class TestMedicineViews(CatalogFactory):
    def setUp(self):
        self.client.force_login(user=self.user)

    def test_medicine_list_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_medicine_list_namespace(self):
        url = reverse("catalog:medicine_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_medicine_detail_url(self):
        response = self.client.get("/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paracetamol")
        self.assertContains(response, "A common painkiller")

    def test_medicine_detail_namespace(self):
        url = reverse(
            "catalog:medicine_detail", kwargs={"medicine_id": self.medicine.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paracetamol")
        self.assertContains(response, "A common painkiller")

    def test_medicine_create_url(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)

    def test_medicine_create_namespace(self):
        url = reverse("catalog:medicine_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_medicine_update_url(self):
        response = self.client.get("/1/update/")
        self.assertEqual(response.status_code, 200)

    def test_medicine_update_namespace(self):
        url = reverse(
            "catalog:medicine_update", kwargs={"medicine_id": self.medicine.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
