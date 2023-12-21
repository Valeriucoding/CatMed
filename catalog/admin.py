from django.contrib import admin
from .models import Disease, MedicationType, BodyOrgan, Medicine, PresentingForm, MedicineProduct

# Register your models here.
admin.site.register(Disease)
admin.site.register(MedicationType)
admin.site.register(BodyOrgan)
admin.site.register(Medicine)
admin.site.register(PresentingForm)
admin.site.register(MedicineProduct)

