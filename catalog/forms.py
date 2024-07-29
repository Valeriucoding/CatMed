from django import forms

from catalog.models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "description", "diseases"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full max-w-xs"}
            ),
            "description": forms.Textarea(
                attrs={"class": "textarea textarea-bordered"}
            ),
            "diseases": forms.SelectMultiple(),
        }


class MedicationTypeForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )


class DiseaseForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )


class BodyOrganForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )
