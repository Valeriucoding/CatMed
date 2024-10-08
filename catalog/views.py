from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicineForm, DiseaseForm, MedicationTypeForm, OrganForm
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


def disease_list_create(request):
    form = DiseaseForm(request.POST or None)
    url = reverse("catalog:disease_list_create")
    context = {
        "form": form,
        "model": "disease",
        "url": url,
        "hx_target": "#diseaseTableBody",
    }
    if request.method == "POST":
        if form.is_valid():
            disease = form.save()
            response = render(
                request,
                "catalog/partials/table_item.html",
                {
                    "model": "disease",
                    "object": disease,
                    "delete_func": "showDiseaseDeleteModal(this)",
                },
            )
            response["HX-Trigger"] = "closeDiseaseCreateModal"
            return response

    html_content = render_to_string(
        "catalog/modals/related_models_modal_form.html", context, request
    )
    return HttpResponse(html_content)


def disease_list(request):
    diseases_list = Disease.objects.all()
    paginator = Paginator(diseases_list, 20)
    page_number = request.GET.get("page")
    diseases = paginator.get_page(page_number)
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

    return render(
        request, "catalog/partials/disease_edit_form.html", {"disease": disease}
    )


def disease_delete(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    if request.method == "DELETE":
        disease.delete()
        # messages.success(request, f"{disease.name} has been successfully deleted.")
        if request.htmx:
            return JsonResponse(
                {"status": "success", "disease_id": disease_id},
                status=200,
            )
        return HttpResponseRedirect(reverse("catalog:disease_list"))
    return HttpResponse(status=405)


def medication_type_create(request):
    form = MedicationTypeForm(request.POST or None)
    url = reverse("catalog:medication_type_create")
    context = {"form": form, "model": "medication_type", "url": url}
    if request.method == "POST":
        if form.is_valid():
            medication_type = form.save()
            return JsonResponse(
                {
                    "id": medication_type.id,
                    "name": medication_type.name,
                    "status": "success",
                    "model": "medication types",
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


def medication_type_list(request):
    medication_types = MedicationType.objects.all()
    paginator = Paginator(medication_types, 20)
    page_number = request.GET.get("page")
    medication_types = paginator.get_page(page_number)
    context = {"medication_types": medication_types}
    if request.htmx:
        return render(
            request, "catalog/partials/medication_type_list_partial.html", context
        )
    return render(request, "catalog/medication_type_list.html", context)


def medication_type_edit(request, medication_type_id):
    medication_type = get_object_or_404(MedicationType, id=medication_type_id)

    if request.method == "POST":
        medication_type.name = request.POST.get("name")
        medication_type.save()
        return render(
            request,
            "catalog/partials/medication_type_display.html",
            {"medication_type": medication_type},
        )

    return render(
        request,
        "catalog/partials/medication_type_edit_form.html",
        {"medication_type": medication_type},
    )


def medication_type_delete(request, medication_type_id):
    medication_type = get_object_or_404(MedicationType, id=medication_type_id)
    if request.method == "DELETE":
        medication_type.delete()
        # messages.success(
        #     request, f"{medication_type.name} has been successfully deleted."
        # )
        if request.htmx:
            return JsonResponse(
                {"status": "success", "medication_type_id": medication_type_id},
                status=200,
            )
        return HttpResponseRedirect(reverse("catalog:medication_type_list"))
    return HttpResponse(status=405)


def medication_type_list_create(request):
    form = MedicationTypeForm(request.POST or None)
    url = reverse("catalog:medication_type_list_create")
    context = {
        "form": form,
        "model": "medication-type",
        "url": url,
        "hx_target": "#medicationTypesTableBody",
    }
    if request.method == "POST":
        if form.is_valid():
            medication_type = form.save()
            response = render(
                request,
                "catalog/partials/table_item.html",
                {
                    "model": "medication-type",
                    "object": medication_type,
                    "delete_func": "showMedicationTypeDeleteModal(this)",
                },
            )
            response["HX-Trigger"] = "closeMedicationTypeCreateModal"
            return response
    html_content = render_to_string(
        "catalog/modals/related_models_modal_form.html", context, request
    )
    return HttpResponse(html_content)


def organ_create(request):
    form = OrganForm(request.POST or None)
    url = reverse("catalog:organ_create")
    context = {"form": form, "model": "body organ", "url": url}
    if request.method == "POST":
        if form.is_valid():
            organ = form.save()
            return JsonResponse(
                {
                    "id": organ.id,
                    "name": organ.name,
                    "status": "success",
                    "model": "organs",
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


def organ_list_create(request):
    form = OrganForm(request.POST or None)
    url = reverse("catalog:organ_list_create")
    context = {
        "form": form,
        "model": "organ",
        "url": url,
        "hx_target": "#organTableBody",
    }

    if request.method == "POST":
        if form.is_valid():
            organ = form.save()
            response = render(
                request,
                "catalog/partials/table_item.html",
                {
                    "model": "organ",
                    "object": organ,
                    "delete_func": "showOrganDeleteModal(this)",
                },
            )
            response["HX-Trigger"] = "closeOrganCreateModal"
            return response
    html_content = render_to_string(
        "catalog/modals/related_models_modal_form.html", context, request
    )
    return HttpResponse(html_content)


def organ_list(request):
    organs_list = Organ.objects.all()
    paginator = Paginator(organs_list, 20)
    page_number = request.GET.get("page")
    organs = paginator.get_page(page_number)
    context = {"organs": organs}
    if request.htmx:
        return render(request, "catalog/partials/organ_list_partial.html", context)
    return render(request, "catalog/organ_list.html", context)


def organ_edit(request, organ_id):
    organ = get_object_or_404(Organ, id=organ_id)

    if request.method == "POST":
        organ.name = request.POST.get("name")
        organ.save()
        return render(request, "catalog/partials/organ_display.html", {"organ": organ})

    return render(request, "catalog/partials/organ_edit_form.html", {"organ": organ})


def organ_delete(request, organ_id):
    organ = get_object_or_404(Organ, id=organ_id)
    if request.method == "DELETE":
        organ.delete()
        # messages.success(request, f"{organ.name} has been successfully deleted.")
        if request.htmx:
            return JsonResponse(
                {"status": "success", "organ_id": organ_id},
                status=200,
            )
        return HttpResponseRedirect(reverse("catalog:organ_list"))
    return HttpResponse(status=405)
