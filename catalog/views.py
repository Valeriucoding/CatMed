from django.shortcuts import render

from catalog.models import Medicine


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, "catalog/medicine_list.html", {"medicines": medicines})
