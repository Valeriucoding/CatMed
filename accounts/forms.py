from allauth.account.forms import ResetPasswordKeyForm

from django import forms
from django.contrib.auth import password_validation


class StyledResetPasswordKeyForm(ResetPasswordKeyForm):
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "input input-bordered w-full", "placeholder": "New password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="New password (again)",
        widget=forms.PasswordInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "New password (again)"}
        ),
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                password_validation.validate_password(password1, self.user)
            except forms.ValidationError as error:
                self.add_error("password1", error)
        return password1
