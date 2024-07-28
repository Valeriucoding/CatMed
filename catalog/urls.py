from django.urls import path

from catalog import views

app_name = "catalog"
urlpatterns = [
    path("", views.medicine_list, name="medicine_list"),
    path("<int:medicine_id>/", views.medicine_detail, name="medicine_detail"),
    path("create/", views.medicine_create, name="medicine_create"),
    path("<int:medicine_id>/update/", views.medicine_update, name="medicine_update"),
    path("<int:medicine_id>/delete/", views.medicine_delete, name="medicine_delete"),
]
