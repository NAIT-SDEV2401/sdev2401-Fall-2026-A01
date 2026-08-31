from django.urls import path
from .views import (
    list_companies, company_detail, employees_search_results, contact_us
)

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    path('company/<int:company_id>/', company_detail, name='company_detail'),
    path('company/<int:company_id>/employees/results/', employees_search_results, name='employees_search_results'),
    path('contact/', contact_us, name='contact_us'),  # New URL pattern for contact form
]
