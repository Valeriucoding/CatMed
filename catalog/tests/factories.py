from django.test import TestCase

from catalog.models import Medicine


class CatalogFactory(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.medicine = Medicine.objects.create(
            name="Paracetamol",
            description="A common painkiller",
        )
