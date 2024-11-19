import json

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicationTypeForm
from catalog.models import MedicationType


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
    if request.method == "POST":
        form = MedicationTypeForm(request.POST)
        if form.is_valid():
            medication_type = form.save()

            # Render the new row
            new_row_html = render_to_string(
                "catalog/partials/table_item.html",
                {
                    "model": "medication-type",
                    "object": medication_type,
                    "delete_func": "showMedicationTypeDeleteModal(this)",
                },
                request=request,
            )

            response = HttpResponse(new_row_html)
            response["HX-Trigger"] = json.dumps({
                "updateMedicationTypesTable": {"html": new_row_html},
                "closeMedicationTypeCreateModal": {}
            })
            return response
    else:
        form = MedicationTypeForm()

    context = {"form": form}
    html_content = render_to_string("catalog/modals/related_models_modal_form.html", context, request)
    return HttpResponse(html_content)
