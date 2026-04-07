from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
   
   path("create-slot/<int:turf_id>/", views.create_slot, name="create_slot"),
    path("join/<int:slot_id>/", views.join_slot, name="join_slot"),
path("slots/<int:turf_id>/", views.slot_list, name="slot_list"),
path("players/<int:slot_id>/", views.view_players, name="view_players"),
path("exit/<int:slot_id>/", views.exit_slot, name="exit_slot"),
path("exit/<int:slot_id>/", views.exit_slot, name="exit_slot"),






]