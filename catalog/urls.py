from django.urls import path

import catalog.views.medicine_views

import catalog.views.disease_views

import catalog.views.medication_type_views

import catalog.views.organ_views
from catalog import views

app_name = "catalog"
urlpatterns = [
    # medicine
    path("", catalog.views.medicine_views.medicine_list, name="medicine_list"),
    path("search/", catalog.views.medicine_views.medicine_search, name="medicine_search"),
    path("<int:medicine_id>/", catalog.views.medicine_views.medicine_detail, name="medicine_detail"),
    path("create/", catalog.views.medicine_views.medicine_create, name="medicine_create"),
    path("<int:medicine_id>/update/", catalog.views.medicine_views.medicine_update, name="medicine_update"),
    path("<int:medicine_id>/delete/", catalog.views.medicine_views.medicine_delete, name="medicine_delete"),
    # disease
    path("diseases/", catalog.views.disease_views.disease_list, name="disease_list"),
    path("disease/create/", catalog.views.disease_views.disease_create, name="disease_create"),
    path(
        "disease/create-table-item",
        catalog.views.disease_views.disease_list_create,
        name="disease_list_create",
    ),
    path("disease/edit/<int:disease_id>/", catalog.views.disease_views.disease_edit, name="disease_edit"),
    path(
        "disease/delete/<int:disease_id>/", catalog.views.disease_views.disease_delete, name="disease_delete"
    ),
    # medication_type
    path(
        "medication_types/create/",
        catalog.views.medication_type_views.medication_type_create,
        name="medication_type_create",
    ),
    path("medication-types/", catalog.views.medication_type_views.medication_type_list, name="medication_type_list"),
    path(
        "medication-types/edit/<int:medication_type_id>/",
        catalog.views.medication_type_views.medication_type_edit,
        name="medication_type_edit",
    ),
    path(
        "medication-types/delete/<int:medication_type_id>/",
        catalog.views.medication_type_views.medication_type_delete,
        name="medication_type_delete",
    ),
    path(
        "medication-types/create-table-item",
        catalog.views.medication_type_views.medication_type_list_create,
        name="medication_type_list_create",
    ),
    # organ
    path("organs/", catalog.views.organ_views.organ_list, name="organ_list"),
    path("organs/edit/<int:organ_id>/", catalog.views.organ_views.organ_edit, name="organ_edit"),
    path("organs/delete/<int:organ_id>/", catalog.views.organ_views.organ_delete, name="organ_delete"),
    path("organs/create-table-item", catalog.views.organ_views.organ_list_create, name="organ_list_create"),
    path("organs/create/", catalog.views.organ_views.organ_create, name="organ_create"),
]
