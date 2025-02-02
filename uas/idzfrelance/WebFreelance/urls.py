from django.contrib import admin
from django.urls import path
from .views import index  # Import the index view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),  # Add URL pattern for the index view
]
