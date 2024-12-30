from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple, AutocompleteSelect
from django.urls import reverse

class CustomAutocompleteSelect(AutocompleteSelect):
    def __init__(self, field, admin_site, attrs=None):
        default_attrs = {"class": "form-control", "style": "width: 100%;"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(field, admin_site, attrs=default_attrs)

    def get_url(self):
        return reverse("catalog:public_admin_autocomplete")


class AutocompleteModelChoiceField(forms.ModelChoiceField):
    """
    A ModelChoiceField with a custom widget that uses an autocomplete view to look up related objects.
    It takes three additional arguments: field_model, form_model, and related_field_name.
    In order to work it needs an admin page for the field_model with search_fields set.
    """

    def __init__(self, field_model, form_model, related_field_name, queryset=None, widget=None, attrs=None, **kwargs):
        if queryset is None:
            queryset = field_model.objects.all()
        if widget is None:
            field = form_model._meta.get_field(related_field_name)
            widget = CustomAutocompleteSelect(field, admin.site, attrs=attrs)
        super().__init__(queryset=queryset, widget=widget, **kwargs)


class CustomAutocompleteSelectMultiple(AutocompleteSelectMultiple):
    def __init__(self, field, admin_site, attrs=None):
        default_attrs = {"class": "form-control", "style": "width: 100%;", "multiple": "multiple"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(field, admin_site, attrs=default_attrs)

    def get_url(self):
        return reverse("catalog:public_admin_autocomplete")


class AutocompleteModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    A ModelMultipleChoiceField with a custom widget that uses an autocomplete view to look up related objects.
    It takes three additional arguments: field_model, form_model, and related_field_name.
    In order to work it needs an admin page for the field_model with search_fields set.
    """

    def __init__(self, field_model, form_model, related_field_name, queryset=None, widget=None, attrs=None, **kwargs):
        if queryset is None:
            queryset = field_model.objects.all()
        if widget is None:
            field = form_model._meta.get_field(related_field_name)
            widget = CustomAutocompleteSelectMultiple(field, admin.site, attrs=attrs)
        super().__init__(queryset=queryset, widget=widget, **kwargs)