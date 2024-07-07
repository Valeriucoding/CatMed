from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.medicine_list, name="medicine_list"),
    path("<int:medicine_id>/", views.medicine_detail, name="medicine_detail"),
]
