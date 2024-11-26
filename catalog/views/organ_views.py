import json

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from catalog.forms import OrganForm
from catalog.models import Organ


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
    if request.method == "POST":
        form = OrganForm(request.POST)
        if form.is_valid():
            organ = form.save()

            # Render the new row
            new_row_html = render_to_string(
                "catalog/components/table_item.html",
                {
                    "model": "organ",
                    "object": organ,
                    "delete_func": "showOrganDeleteModal(this)",
                },
                request=request,
            )

            response = HttpResponse(new_row_html)
            response["HX-Trigger"] = json.dumps({"updateOrganTable": {"html": new_row_html}, "closeOrganCreateModal": {}})
            return response
    else:
        form = OrganForm()

    context = {"form": form}
    html_content = render_to_string("catalog/modals/related_models_modal_form.html", context, request)
    return HttpResponse(html_content)


def organ_list(request):
    organs_list = Organ.objects.all()
    paginator = Paginator(organs_list, 17)
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
