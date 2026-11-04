from django.urls import path

from .views import update_profile, profile_list

urlpatterns = [
    path('edit/', update_profile, name='profile_edit'),
    path('', profile_list, name='profile_list')
]