from catalog.models import MedicineProduct
from factories import CatalogFactory


class TestMedicineProduct(CatalogFactory):
    def test_zenyth_get_medicine_product_info(self):
        self.medicine_product = MedicineProduct.objects.create(
            medicine=self.medicine,
            product_url="https://zenyth.ro/produse/vitamina-c-premium-cu-rodie-bioflavonoide-si-resveratrol-30-capsule-1000-mg/",
        )
        self.assertEqual(self.medicine_product.name, "Vitamina C Premium cu rodie, 1000 mg, 30 cps.")