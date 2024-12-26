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
    autocomplete_fields = ("diseases",)

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(MedicationType)
admin.site.register(Organ)
admin.site.register(PresentingForm)
admin.site.register(MedicineProduct)
