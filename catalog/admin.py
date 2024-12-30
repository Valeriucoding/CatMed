from django.contrib import admin

from .models import (
    Disease,
    MedicationType,
    Organ,
    Medicine,
    PresentingForm,
    MedicineProduct,
)

from django.contrib.admin import AdminSite


class PublicAdminSite(AdminSite):
    site_header = "Public Autocomplete"
    site_title = "Public Autocomplete Site"
    index_title = "Public Autocomplete Index"

public_admin = PublicAdminSite(name='public_admin')

@admin.register(Medicine, site=public_admin)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    autocomplete_fields = ("diseases", "medication_types", "organs")

@admin.register(Disease, site=public_admin)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(MedicationType, site=public_admin)
class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Organ, site=public_admin)
class OrganAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(PresentingForm, site=public_admin)
class PresentingFormAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(MedicineProduct, site=public_admin)
class MedicineProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

