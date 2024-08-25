from django.db import models
from django.urls import reverse


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class MedicationType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class BodyOrgan(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    diseases = models.ManyToManyField(Disease, related_name="medicines", blank=True)
    medication_types = models.ManyToManyField(
        MedicationType, related_name="medicines", blank=True
    )
    body_organs = models.ManyToManyField(
        BodyOrgan, related_name="medicines", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:medicine_detail", args=[self.id])


class PresentingForm(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capsules = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MedicineProduct(models.Model):
    BUY_PLACES = (
        ("F", "farmacie"),
        ("P", "plafar"),
        ("S", "site"),
    )
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, related_name="medicine_products"
    )
    name = models.CharField(max_length=255, unique=True)
    buy_place = models.CharField(
        max_length=100, choices=BUY_PLACES, blank=True, null=True
    )
    product_url = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    method_of_administration = models.TextField(null=True, blank=True)
    presenting_form = models.ForeignKey(
        PresentingForm, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
