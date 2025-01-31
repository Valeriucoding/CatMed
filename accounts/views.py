from allauth.account.views import LoginView, SignupView, LogoutView


class HTMXLoginView(LoginView):
    template_name = "account/login.html"
    partial_template_name = "account/partials/login_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get('HX-Request'):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)


class HTMXSignupView(SignupView):
    template_name = "account/signup.html"
    partial_template_name = "account/partials/signup_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get('HX-Request'):
            print("HTMX request detected")
            self.template_name = self.partial_template_name
        print("Full page request detected")
        return super().get(request, *args, **kwargs)

class HTMXLogoutView(LogoutView):
    template_name = "account/logout.html"
    partial_template_name = "account/partials/logout_partial.html"

    def get(self, request, *args, **kwargs):
        if request.headers.get('HX-Request'):
            self.template_name = self.partial_template_name
        return super().get(request, *args, **kwargs)