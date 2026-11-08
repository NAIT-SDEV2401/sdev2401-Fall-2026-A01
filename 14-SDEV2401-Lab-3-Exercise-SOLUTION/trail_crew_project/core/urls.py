from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    # STUDENT TODO: add login and logout urls
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

