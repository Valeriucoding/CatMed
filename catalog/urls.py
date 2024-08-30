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
    path("medication-types/", views.medication_type_list, name="medication_type_list"),
    path(
        "medication-types/edit/<int:medication_type_id>/",
        views.medication_type_edit,
        name="medication_type_edit",
    ),
    path(
        "medication-types/delete/<int:medication_type_id>/",
        views.medication_type_delete,
        name="medication_type_delete",
    ),
    path(
        "medication-types/create-table-item",
        views.medication_type_list_create,
        name="medication_type_list_create",
    ),
    # organ
    path("organs/", views.organ_list, name="organ_list"),
    path("organs/edit/<int:organ_id>/", views.organ_edit, name="organ_edit"),
    path("organs/delete/<int:organ_id>/", views.organ_delete, name="organ_delete"),
    path("organs/create-table-item", views.organ_list_create, name="organ_list_create"),
    path("organs/create/", views.organ_create, name="organ_create"),
]
