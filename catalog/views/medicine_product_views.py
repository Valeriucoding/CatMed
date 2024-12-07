from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import MedicineProductForm


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