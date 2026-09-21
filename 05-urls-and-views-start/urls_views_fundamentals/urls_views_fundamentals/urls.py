from django.contrib import admin
from django.urls import path, include # include is used to include urls from other apps
# import the urls from the pet_adoption app
from pet_adoption import urls as pet_adoption_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    # include the urls from the pet_adoption app
    # this means that it's
    path("", include(pet_adoption_urls)),
]
