from django.urls import path
from .views import HTMXLoginView, HTMXSignupView, HTMXLogoutView

urlpatterns = [
    path("accounts/login/", HTMXLoginView.as_view(), name="account_login"),
    path("accounts/signup/", HTMXSignupView.as_view(), name="account_signup"),
    path("accounts/logout/", HTMXLogoutView.as_view(), name="account_logout"),
]
