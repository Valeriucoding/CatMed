import json

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import DiseaseForm
from catalog.models import Disease


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
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save()

            # Render the new row
            new_row_html = render_to_string(
                "catalog/components/table_item.html",
                {
                    "model": "disease",
                    "object": disease,
                    "delete_func": "showDiseaseDeleteModal(this)",
                },
                request=request,
            )

            response = HttpResponse(new_row_html)
            response["HX-Trigger"] = json.dumps({
                "updateDiseaseTable": {"html": new_row_html},
                "closeDiseaseCreateModal": {}
            })
            return response
    else:
        form = DiseaseForm()

    context = {"form": form,}
    html_content = render_to_string("catalog/modals/related_models_modal_form.html", context, request)
    return HttpResponse(html_content)


def disease_list(request):
    diseases_list = Disease.objects.all()
    paginator = Paginator(diseases_list, 17)
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
