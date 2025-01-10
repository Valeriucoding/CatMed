import json

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicineProductForm
from catalog.models import MedicineProduct


def medicine_product_create(request, medicine_pk):
    form = MedicineProductForm(request.POST or None)
    url = reverse("catalog:medicine_product_create", kwargs={"medicine_pk": medicine_pk})
    context = {"form": form, "model": "medicine product", "url": url}
    if request.method == "POST":
        if form.is_valid():
            medicine_product = form.save(commit=False)
            medicine_product.medicine_id = medicine_pk
            medicine_product.save()
            new_row_html = render_to_string("catalog/components/medicine_product_table_item.html", {"product": medicine_product}, request=request)

            response = HttpResponse(new_row_html)
            response["HX-Trigger"] = json.dumps({"addMedicineProductTableComponent": {"html": new_row_html}})
            return response
        else:
            html_content = render_to_string(
                "catalog/modals/modal_form.html", context, request
            )
            return HttpResponse(html_content)
    html_content = render_to_string("catalog/modals/medicine_product_create.html", context, request)
    return HttpResponse(html_content)

def medicine_product_delete(request, medicine_product_pk):
    if request.method == "DELETE":
        medicine_product = get_object_or_404(MedicineProduct, pk=medicine_product_pk)
        medicine_product.delete()
        if request.htmx:
            return JsonResponse({"status": "success", "medicine_product_pk": medicine_product_pk}, status=200)
        return HttpResponseRedirect(reverse("catalog:medicine_detail", args=[medicine_product.medicine.id]))
    return JsonResponse({"status": "error"}, status=400)


def medicine_product_update(request, medicine_product_pk):
    medicine_product = get_object_or_404(MedicineProduct, pk=medicine_product_pk)
    if request.method == "POST":
        form = MedicineProductForm(request.POST, instance=medicine_product)
        if form.is_valid():
            form.save()
            new_row_html = render_to_string("catalog/components/medicine_product_table_item.html", {"product": medicine_product}, request=request)
            response = HttpResponse(new_row_html)
            response["HX-Trigger"] = json.dumps({"updateMedicineProductTable": {"html": new_row_html}})
            return response
        else:
            context = {"form": form, "model": "medicine product", "url": reverse("catalog:medicine_product_update", kwargs={"medicine_product_pk": medicine_product_pk})}
            html_content = render_to_string("catalog/modals/modal_form.html", context, request)
            return HttpResponse(html_content)
    else:
        form = MedicineProductForm(instance=medicine_product)
    context = {"form": form, "test": "123"}
    html_content = render_to_string("catalog/modals/related_models_modal_form.html", context, request)
    return HttpResponse(html_content)
        