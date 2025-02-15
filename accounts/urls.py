from django.urls import path

from accounts.views import (
    HTMXLoginView,
    HTMXLogoutView,
    HTMXSignupView,
    user_profile,
)


urlpatterns = [
    path("accounts/login/", HTMXLoginView.as_view(), name="account_login"),
    path("accounts/signup/", HTMXSignupView.as_view(), name="account_signup"),
    path("accounts/logout/", HTMXLogoutView.as_view(), name="account_logout"),
    path("accounts/profile/", user_profile, name="user_profile"),
]
