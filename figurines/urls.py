from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "figurines"

urlpatterns = [
    path("add_figurine/", views.add_figurine, name="add_figurine"),
]
