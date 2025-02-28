import posthog
from allauth.account.views import (
    LoginView,
    LogoutView,
    SignupView,
)

from django.shortcuts import render


class HTMXLoginView(LoginView):
    template_name = "account/login.html"
    partial_template_name = "account/partials/login_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        posthog.identify(user.id, {"email": user.email})
        posthog.capture(user.id, "User Logged In")
        return response


class HTMXSignupView(SignupView):
    template_name = "account/signup.html"
    partial_template_name = "account/partials/signup_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.user
        posthog.identify(user.id, {"email": user.email})
        posthog.capture(user.id, "User Signed Up")
        return response


class HTMXLogoutView(LogoutView):
    template_name = "account/logout.html"
    partial_template_name = "account/partials/logout_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            posthog.capture(request.user.id, "User Logged Out")
        return super().dispatch(request, *args, **kwargs)


def user_profile(request):
    if request.htmx:
        return render(
            request,
            "account/partials/user_profile_card_partial.html",
        )
    return render(request, "account/user_profile_card.html")
