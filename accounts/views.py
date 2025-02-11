import posthog
from allauth.account.views import (
    LoginView,
    LogoutView,
    PasswordResetFromKeyView,
    PasswordResetView,
    SignupView,
)


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


class HTMXForgotPasswordView(PasswordResetView):
    template_name = "account/password_reset.html"
    partial_template_name = "account/partials/password_reset_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        response = super().post(request, *args, **kwargs)
        email = request.POST.get("email")
        posthog.capture(email, "Password Reset Requested")
        return response


class HTMXPasswordResetConfirmView(PasswordResetFromKeyView):
    template_name = "account/password_reset_confirm.html"
    partial_template_name = "account/partials/password_reset_confirm_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        response = super().post(request, *args, **kwargs)
        user = request.user if request.user.is_authenticated else None
        if user:
            posthog.capture(user.id, "Password Reset Confirmed")
        return response
