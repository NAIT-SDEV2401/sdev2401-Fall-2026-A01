from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("organizer", "Organizer"),
        ("presenter", "Presenter"),
    )
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="organizer")
    full_name = models.CharField(max_length=150, blank=True, default="")
    bio = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return f"{self.username} ({self.role})"
