from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO Part 1: Add path("v1/auth/", include("djoser.urls"))
    # TODO Part 1: Add path("v1/auth/", include("djoser.urls.authtoken"))
    # TODO Part 2: Add path("v1/api/", include("events.urls"))
]
