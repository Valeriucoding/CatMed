from django.contrib import admin

from .models import (
    Disease,
    MedicationType,
    Organ,
    Medicine,
    PresentingForm,
    MedicineProduct,
)


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(MedicationType)
admin.site.register(Organ)
admin.site.register(Medicine)
admin.site.register(PresentingForm)
admin.site.register(MedicineProduct)
