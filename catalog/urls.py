from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.medicine_list, name="medicine_list"),
]
