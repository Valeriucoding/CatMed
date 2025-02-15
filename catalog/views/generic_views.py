from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from catalog.forms import ContactForm


def contact_form(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            send_mail(
                f"New Contact Form Submission from {name}",
                message,
                email,
                [settings.DEFAULT_TO_EMAIL],
            )
            response = HttpResponse(status=204)
            response.headers["HX-Trigger"] = "contactFormSuccess"
            return response
    if request.htmx:
        return render(request, "catalog/partials/contact_form_partial.html", {"form": form})
    return render(request, "catalog/contact_form.html", {"form": form})
