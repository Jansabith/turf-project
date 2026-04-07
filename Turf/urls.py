from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
   path("create_turf/",views.create_turf,name="create_turf"),
   path("turf/<int:id>/", views.turf_detail, name="turf_detail"),
   path("delete-turf/<int:turf_id>/", views.delete_turf, name="delete_turf"),
   path("delete-slot/<int:slot_id>/", views.delete_slot, name="delete_slot"),
   path("edit_turf/<int:turf_id>/", views.edit_turf, name="edit_turf"),
   



]