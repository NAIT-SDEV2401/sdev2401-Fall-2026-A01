from django.urls import path
from .views import home_page, pet_type_details

urlpatterns = [
    path("", home_page, name="home_page"),
    # detail page
    path("pet_type/<str:pet_type>/", pet_type_details, name="pet_type_details"),
]
