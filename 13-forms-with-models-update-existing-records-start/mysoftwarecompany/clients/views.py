from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail

# get the specical function to fetch an object or return a 404 error
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Company, Employee
from .forms import ContactForm, CompanyForm

def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        # check if the form is valid.
        if form.is_valid():
            # Save the new company to the database
            # this uses the clean data from the form to create a new company
            form.save()

            company = form.instance  # Get the newly created company instance
            # pass the new company to the template
            return render(request,
                "clients/create_company.html",
                {"form": CompanyForm(), "new_company": company}
            )
        else:
            return render(request,
                "clients/create_company.html",
                {"form": form}
            )
    if request.method == "GET":
        form = CompanyForm()
        return render(request,
            "clients/create_company.html",
            {"form": form}
        )


# Create the contact form here.
def contact_us(request):
    # this handles get request and displays the form to the user.
    if request.method == "GET":
        form = ContactForm()
        return render(request,
            "clients/contact_us.html",
            {"form": form}
        )
    # form submission will be handled in future steps.
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email to some_admin_account@test.com
            send_mail(
                subject=f'Contact Us Message from {name}',
                message=message,
                from_email=email,
                recipient_list=['some_admin_account@test.com'],
                fail_silently=False,
            )
            return render(request,
                "clients/contact_us.html",
                {"form": ContactForm(), "success": True}
            )
        else:
            return render(request,
                "clients/contact_us.html",
                {"form": form}
            )

def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()
    return render(request, 'clients/companies_list.html', {'companies': companies})

def company_detail(request, company_id):
    # fetching a specific company by its ID or returning a 404 error if not found
    # note: we haven't discussed this but every single model in django
    # has a unique "id" field by default which is an auto-incrementing integer
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'clients/company_detail.html', {'company': company})


def employees_search_results(request, company_id):
    # this is going to handle the search query for employees
    query = request.GET.get('q', '')

    company = get_object_or_404(Company, id=company_id)
    # this is going to handle the search query for employees

    if query:
        # If a query is provided, filter employees by first name
        # using icontains for case-insensitive search
        employees = Employee.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
    else:
        # If no query is provided, return an empty queryset
        employees = Employee.objects.none()
    # return
    return render(request, 'clients/employees_search_results.html',
                  {'employees': employees, 'query': query, 'company': company})