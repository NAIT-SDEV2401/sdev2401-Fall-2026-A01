from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # STUDENT TODO: Include the app_found_items URLs under v1/api/.
]
