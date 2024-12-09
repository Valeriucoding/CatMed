from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicineProductForm
from catalog.models import MedicineProduct


def medicine_product_create(request):
    form = MedicineProductForm(request.POST or None)
    url = reverse("catalog:medicine_product_create")
    context = {"form": form, "model": "medicine product", "url": url}
    if request.method == "POST":
        if form.is_valid():
            medicine_product = form.save()
            return JsonResponse(
                {
                    "id": medicine_product.id,
                    "name": medicine_product.name,
                    "status": "success",
                    "model": "medicine products",
                },
                status=200,
            )
        else:
            html_content = render_to_string(
                "catalog/modals/modal_form.html", context, request
            )
            return HttpResponse(html_content)

def medicine_product_delete(request, medicine_product_pk):
    if request.method == "DELETE":
        medicine_product = get_object_or_404(MedicineProduct, pk=medicine_product_pk)
        medicine_product.delete()
        if request.htmx:
            return JsonResponse({"status": "success", "medicine_product_pk": medicine_product_pk}, status=200)
        return HttpResponseRedirect(reverse("catalog:medicine_detail", args=[medicine_product.medicine.id]))
    return JsonResponse({"status": "error"}, status=400)