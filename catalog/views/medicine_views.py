from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from catalog.forms import MedicineForm
from catalog.models import Medicine, Disease, MedicationType, Organ


def medicine_list(request):
    medicines = Medicine.objects.all().prefetch_related("diseases", "medication_types")
    disease_ids = request.GET.getlist("disease")
    medication_type_ids = request.GET.getlist("medication-type")
    organ_ids = request.GET.getlist("organ")

    diseases_params = []

    if disease_ids:
        medicines = medicines.filter(diseases__id__in=disease_ids).distinct()
        diseases = Disease.objects.filter(id__in=disease_ids)
        diseases_params = list(diseases)

    medication_types_params = []
    if medication_type_ids:
        medicines = medicines.filter(
            medication_types__id__in=medication_type_ids
        ).distinct()
        medication_types = MedicationType.objects.filter(id__in=medication_type_ids)
        medication_types_params = list(medication_types)

    organs_params = []
    if organ_ids:
        medicines = medicines.filter(organs__id__in=organ_ids).distinct()
        organs = Organ.objects.filter(id__in=organ_ids)
        organs_params = list(organs)

    context = {
        "medicines": medicines,
        "diseases_params": diseases_params,
        "medication_types_params": medication_types_params,
        "organs_params": organs_params,
    }

    storage = messages.get_messages(request)
    if storage:
        context["alert_message"] = list(storage)[0]
        storage.used = True

    return render(
        request,
        (
            "catalog/partials/medicine_list_partial.html"
            if request.htmx
            else "catalog/medicine_list.html"
        ),
        context,
    )


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
    form = MedicineForm(request.POST or None)
    url = reverse("catalog:medicine_create")
    context = {
        "form": form,
        "title": "Create Medicine",
        "action": "Create",
        "url": url,
        "back_url": reverse("catalog:medicine_list"),
    }
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
                request, "catalog/partials/medicine_form_partial.html", context
            )

    if request.htmx:
        return render(
            request,
            "catalog/partials/medicine_form_partial.html",
            context,
        )

    return render(request, "catalog/medicine_form.html", context)


def medicine_update(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    form = MedicineForm(request.POST or None, instance=medicine)
    url = reverse("catalog:medicine_update", args=[medicine.id])
    context = {
        "form": form,
        "title": "Update Medicine",
        "action": "Update",
        "url": url,
        "back_url": medicine.get_absolute_url(),
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
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
                request, "catalog/partials/medicine_form_partial.html", context
            )

    if request.htmx:
        return render(request, "catalog/partials/medicine_form_partial.html", context)

    return render(request, "catalog/medicine_form.html", context)


def medicine_delete(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == "DELETE":
        medicine.delete()
        messages.success(request, f"{medicine.name} has been successfully deleted.")
        if request.htmx:
            return HttpResponse(
                status=200, headers={"HX-Redirect": reverse("catalog:medicine_list")}
            )
        return HttpResponseRedirect(reverse("catalog:medicine_list"))
    return HttpResponse(status=405)


def medicine_search(request):
    q = request.GET.get("q")

    if q:
        medicines = Medicine.objects.filter(name__icontains=q)
    else:
        medicines = Medicine.objects.all()

    context = {"medicines": medicines}
    return render(request, "catalog/components/medicine_card.html", context)