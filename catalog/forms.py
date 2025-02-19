from django import forms

from catalog.models import Medicine, Disease, MedicationType, Organ, MedicineProduct
from utils.forms import AutocompleteModelMultipleChoiceField


class MedicineForm(forms.ModelForm):
    diseases = AutocompleteModelMultipleChoiceField(field_model=Disease, form_model=Medicine, related_field_name="diseases", required=False)
    medication_types = AutocompleteModelMultipleChoiceField(field_model=MedicationType, form_model=Medicine, related_field_name="medication_types", required=False)
    organs = AutocompleteModelMultipleChoiceField(field_model=Organ, form_model=Medicine, related_field_name="organs", required=False)
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


class MedicineProductForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}))

    class Meta:
        model = MedicineProduct
        fields = ["name", "product_url", "price", "currency", "notes"]
        widgets = {
            "product_url": forms.URLInput(attrs={"class": "input input-bordered w-full"}),
            "price": forms.NumberInput(attrs={"class": "input input-bordered w-full", "required": False}),
            "currency": forms.Select(attrs={"class": "input input-bordered w-full"}),
            "notes": forms.Textarea(attrs={"class": "textarea textarea-bordered w-full", "style": "height: 100px;"})
        }

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "input input-bordered w-full",
            "placeholder": "Your name"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "input input-bordered w-full",
            "placeholder": "Your email"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "textarea textarea-bordered w-full",
            "rows": 5,
            "placeholder": "Your message"
        })
    )