from allauth.account.views import LoginView, LogoutView, PasswordResetFromKeyView, PasswordResetView, SignupView


class HTMXLoginView(LoginView):
    template_name = "account/login.html"
    partial_template_name = "account/partials/login_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)


class HTMXSignupView(SignupView):
    template_name = "account/signup.html"
    partial_template_name = "account/partials/signup_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)


class HTMXLogoutView(LogoutView):
    template_name = "account/logout.html"
    partial_template_name = "account/partials/logout_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)


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
        return super().post(request, *args, **kwargs)


class HTMXPasswordResetConfirmView(PasswordResetFromKeyView):
    # TODO: not working rn
    template_name = "account/password_reset_confirm.html"
    partial_template_name = "account/partials/password_reset_confirm_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.headers.get("HX-Request"):
            self.template_name = self.partial_template_name
        return super().post(request, *args, **kwargs)
