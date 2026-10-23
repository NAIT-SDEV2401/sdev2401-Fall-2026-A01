from django.urls import path
from .views import (
    list_companies, company_detail, employees_search_results, contact_us,
    create_company, update_company
)

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    path('company/<int:company_id>/', company_detail, name='company_detail'),
    path('company/<int:company_id>/employees/results/', employees_search_results, name='employees_search_results'),
    path('company/create/', create_company, name='create_company'),
    path('contact/', contact_us, name='contact_us'),
    path('company/<int:company_id>/update/', update_company, name='update_company') 
]
