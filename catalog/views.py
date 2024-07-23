from django.shortcuts import render

from catalog.models import Medicine


def medicine_list(request):
    medicines = Medicine.objects.all()
    if request.htmx:
        return render(
            request, "catalog/medicine_list_partial.html", {"medicines": medicines}
        )
    return render(request, "catalog/medicine_list.html", {"medicines": medicines})


def medicine_detail(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.htmx:
        return render(
            request, "catalog/medicine_detail_partial.html", {"medicine": medicine}
        )
    return render(request, "catalog/medicine_detail.html", {"medicine": medicine})
