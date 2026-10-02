from django.shortcuts import render
from .models import Company

def list_companies(request):
    the_companies = Company.objects.all();
    return render(request, "clients/companies_list.html", {'companies': the_companies})