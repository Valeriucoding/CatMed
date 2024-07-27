from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from catalog.forms import MedicineForm
from catalog.models import Medicine


def medicine_list(request):
    medicines = Medicine.objects.all()
    if request.htmx:
        return render(
            request,
            "catalog/partials/medicine_list_partial.html",
            {"medicines": medicines},
        )
    return render(request, "catalog/medicine_list.html", {"medicines": medicines})


def medicine_detail(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.htmx:
        return render(
            request,
            "catalog/partials/medicine_detail_partial.html",
            {"medicine": medicine},
        )
    return render(request, "catalog/medicine_detail.html", {"medicine": medicine})


def medicine_create(request):
    form = MedicineForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return render(
                request, "catalog/partials/medicine_form_partial.html", {"form": form}
            )

    if request.htmx:
        return render(
            request,
            "catalog/partials/medicine_form_partial.html",
            {"form": form},
        )

    return render(request, "catalog/medicine_form.html", {"form": form})


def medicine_create(request):
    form = MedicineForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            medicine = form.save()
            if request.htmx:
                return HttpResponse(
                    status=200,
                    headers={
                        "HX-Redirect": reverse(
                            "catalog:medicine_detail", args=[medicine.id]
                        )
                    },
                )
            return HttpResponseRedirect(
                reverse("catalog:medicine_detail", args=[medicine.id])
            )
        else:
            return render(
                request, "catalog/partials/medicine_form_partial.html", {"form": form}
            )

    if request.htmx:
        return render(
            request,
            "catalog/partials/medicine_form_partial.html",
            {"form": form},
        )

    return render(request, "catalog/medicine_form.html", {"form": form})
