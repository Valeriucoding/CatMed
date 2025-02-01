from django.urls import path

from .views import HTMXLoginView, HTMXLogoutView, HTMXPasswordResetConfirmView, HTMXSignupView


urlpatterns = [
    path("accounts/login/", HTMXLoginView.as_view(), name="account_login"),
    path("accounts/signup/", HTMXSignupView.as_view(), name="account_signup"),
    path("accounts/logout/", HTMXLogoutView.as_view(), name="account_logout"),
    path("accounts/password/reset/", HTMXLogoutView.as_view(), name="account_password_reset"),
    path(
        "accounts/password/reset/confirm/<uidb64>/<token>/",
        HTMXPasswordResetConfirmView.as_view(),
        name="account_reset_password_from_key",
    ),
]
