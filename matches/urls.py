from django.urls import path
from . import views

urlpatterns = [

    path("teams/<int:slot_id>/", views.view_teams, name="view_teams"),

]