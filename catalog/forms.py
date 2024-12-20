from django import forms

from catalog.models import Medicine, Disease, MedicationType, Organ


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "description", "diseases", "medication_types", "organs"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full max-w-xs"}
            ),
            "description": forms.Textarea(
                attrs={"class": "textarea textarea-bordered"}
            ),
            "diseases": forms.CheckboxSelectMultiple(attrs={"class": "checkbox"}),
            "medication_types": forms.CheckboxSelectMultiple(
                attrs={"class": "checkbox"}
            ),
            "organs": forms.CheckboxSelectMultiple(attrs={"class": "checkbox"}),
        }


class MedicationTypeForm(forms.ModelForm):
    class Meta:
        model = MedicationType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"})
        }


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"})
        }


class OrganForm(forms.ModelForm):
    class Meta:
        model = Organ
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"})
        }
