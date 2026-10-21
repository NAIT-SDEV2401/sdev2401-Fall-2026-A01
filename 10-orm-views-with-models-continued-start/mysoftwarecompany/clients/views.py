from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Company, Employee

def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()

    return render(request, 'clients/companies_list.html', {'companies': companies})

def company_detail(request, company_id):
    the_company = get_object_or_404(Company, id=company_id)
    return render(request, 'clients/company_detail.html', {'company': the_company})

def employees_search_results(request, company_id):
    # this is going to handle the search query for employees
    query = request.GET.get('q', '')
    company = get_object_or_404(Company, id=company_id)

    if query:
        # region query explanation
        # If a query is provided, filter employees by first name
        # using icontains for case-insensitive search
        # company.employees is a queryset of employees related to the company
         # and we filter it by first_name__icontains=query
         # this will return all employees whose first name contains the query string
         # endregion
        employees = company.employees.filter(
            first_name__icontains=query
         )
    else:
        # If no query is provided, return an empty queryset
        employees = Employee.objects.none()
    # return
    return render(request, 'clients/employees_search_results.html', {'employees': employees, 'query': query})
