
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('core.urls')),
    path("announcements/", include('announcements.urls'))
]
