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

class MedicineAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    autocomplete_fields = ("diseases", "medication_types", "organs")

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class OrganAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class PresentingFormAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class MedicineProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(MedicationType, MedicationTypeAdmin)
admin.site.register(Organ, OrganAdmin)
admin.site.register(PresentingForm, PresentingFormAdmin)
admin.site.register(MedicineProduct, MedicineProductAdmin)

public_admin.register(Medicine, MedicineAdmin)
public_admin.register(Disease, DiseaseAdmin)
public_admin.register(MedicationType, MedicationTypeAdmin)
public_admin.register(Organ, OrganAdmin)
public_admin.register(PresentingForm, PresentingFormAdmin)
public_admin.register(MedicineProduct, MedicineProductAdmin)