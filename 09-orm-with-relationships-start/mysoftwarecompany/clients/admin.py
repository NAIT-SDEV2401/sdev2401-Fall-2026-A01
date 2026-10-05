from django.contrib import admin
from .models import Company, Employee

# this is going to add it to the admin interface.
admin.site.register(Company)
admin.site.register(Employee)