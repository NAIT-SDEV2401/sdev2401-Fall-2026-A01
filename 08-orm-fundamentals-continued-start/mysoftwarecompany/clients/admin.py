from django.contrib import admin
from .models import Company

# this is going to add it to the admin interface.
admin.site.register(Company)