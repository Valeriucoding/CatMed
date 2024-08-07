from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicineForm, DiseaseForm
from catalog.models import Medicine, Disease


def medicine_list(request):
    medicines = Medicine.objects.all()
    context = {"medicines": medicines}

    # Check for messages
    storage = messages.get_messages(request)
    if storage:
        # Add the first message to the context
        context["alert_message"] = list(storage)[0]
        storage.used = True

    if request.htmx:
        return render(request, "catalog/partials/medicine_list_partial.html", context)
    return render(request, "catalog/medicine_list.html", context)


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


def disease_create(request):
    form = DiseaseForm(request.POST or None)
    url = reverse("catalog:disease_create")
    context = {"form": form, "model": "disease", "url": url}
    if request.method == "POST":
        if form.is_valid():
            disease = form.save()
            return JsonResponse(
                {
                    "id": disease.id,
                    "name": disease.name,
                    "status": "success",
                    "model": "diseases",
                },
                status=200,
            )
        else:

            html_content = render_to_string(
                "catalog/modals/modal_form.html", context, request
            )
            return HttpResponse(html_content)

    html_content = render_to_string("catalog/modals/modal_form.html", context, request)
    return HttpResponse(html_content)


def disease_list(request):
    diseases = Disease.objects.all()
    context = {"diseases": diseases}
    if request.htmx:
        return render(request, "catalog/partials/disease_list_partial.html", context)
    return render(request, "catalog/disease_list.html", context)


def disease_edit(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)

    if request.method == "POST":
        disease.name = request.POST.get("name")
        disease.save()
        return render(
            request, "catalog/partials/disease_display.html", {"disease": disease}
        )

    return render(request, "catalog/partials/disease_form.html", {"disease": disease})


def disease_delete(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    if request.method == "DELETE":
        disease.delete()
        messages.success(request, f"{disease.name} has been successfully deleted.")
        if request.htmx:
            return HttpResponse(
                status=200, headers={"HX-Redirect": reverse("catalog:disease_list")}
            )
        return HttpResponseRedirect(reverse("catalog:disease_list"))
    return HttpResponse(status=405)
