from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    # STUDENT TODO: add login and logout urls

]

