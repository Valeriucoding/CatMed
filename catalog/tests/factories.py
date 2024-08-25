from django.test import TestCase

from catalog.models import Medicine, Disease, MedicationType


class CatalogFactory(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.medicine = Medicine.objects.create(
            name="Paracetamol",
            description="A common painkiller",
        )
        cls.disease = Disease.objects.create(name="Headache")
        cls.medicine.diseases.add(cls.disease)
        cls.medication_type = MedicationType.objects.create(name="Tablet")
        cls.medicine.medication_types.add(cls.medication_type)
