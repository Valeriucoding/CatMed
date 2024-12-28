from django.contrib import admin

from .models import (
    Disease,
    MedicationType,
    Organ,
    Medicine,
    PresentingForm,
    MedicineProduct,
)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    autocomplete_fields = ("diseases", "medication_types", "organs")

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(MedicationType)
class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(PresentingForm)
class PresentingFormAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(MedicineProduct)
class MedicineProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

