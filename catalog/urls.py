from django.urls import path

from catalog import views

app_name = "catalog"
urlpatterns = [
    # medicine
    path("", views.medicine_list, name="medicine_list"),
    path("<int:medicine_id>/", views.medicine_detail, name="medicine_detail"),
    path("create/", views.medicine_create, name="medicine_create"),
    path("<int:medicine_id>/update/", views.medicine_update, name="medicine_update"),
    path("<int:medicine_id>/delete/", views.medicine_delete, name="medicine_delete"),
    # disease
    path("diseases/", views.disease_list, name="disease_list"),
    path("disease/create/", views.disease_create, name="disease_create"),
    path(
        "disease/create-table-item",
        views.disease_list_create,
        name="disease_list_create",
    ),
    path("disease/edit/<int:disease_id>/", views.disease_edit, name="disease_edit"),
    path(
        "disease/delete/<int:disease_id>/", views.disease_delete, name="disease_delete"
    ),
    # medication_type
    path(
        "medication_types/create/",
        views.medication_type_create,
        name="medication_type_create",
    ),
    # body_organ
    path("body_organs/create/", views.body_organ_create, name="body_organ_create"),
]
