from django.urls import path

from accounts.views import (
    HTMXLoginView,
    HTMXLogoutView,
    HTMXSignupView,
    user_profile,
)


urlpatterns = [
    path("login/", HTMXLoginView.as_view(), name="account_login"),
    path("signup/", HTMXSignupView.as_view(), name="account_signup"),
    path("logout/", HTMXLogoutView.as_view(), name="account_logout"),
    path("profile/", user_profile, name="user_profile"),
]
