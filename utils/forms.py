from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django.forms import ModelForm
from django.urls import reverse


class BaseModelForm(ModelForm):
    def __init__(self, *args, load_related_only=False, **kwargs):
        super().__init__(*args, **kwargs)

        if load_related_only and self.instance.pk:
            for field_name, field in self.fields.items():
                if isinstance(field, AutocompleteModelChoiceField):
                    related_value = getattr(self.instance, field_name)
                    if related_value:
                        field.queryset = field.queryset.model.objects.filter(pk=related_value.pk)


class CustomAutocompleteSelect(AutocompleteSelect):
    def __init__(self, field, admin_site, attrs=None):
        default_attrs = {"class": "form-control", "style": "width: 100%;"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(field, admin_site, attrs=default_attrs)

    def get_url(self):
        return reverse("admin:autocomplete")


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