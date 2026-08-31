# Django ORM - More ORM usage, filters, views, and data management commands

So far we've learned a lot about the Object-Relational Mapping (ORM) in Django, including how to create models, define relationships, and perform basic CRUD operations.

In this example, we will continue exploring the ORM with a focus on views, advanced filtering, and data management.

## Prerequisites
- Create a new virtual environment and install the packages from the `requirements.txt` file.

- Review the last example and concepts.

## Steps

### 1. We're going to load data into a fresh database.
We deleted the database from the last few examples, but we have all of the data in the `clients_data.json` file. We can load this data into our database using the `loaddata` command.

Let's first create our new database by applying the migrations:
```bash
python manage.py migrate
```
Let's create a superuser to access the admin interface:
```bash
python manage.py createsuperuser
```
- Follow the prompts to create a superuser account.

Now we can load the data into our database:
```bash
python manage.py loaddata clients_data.json
```
- This is going to read the `clients_data.json` file and populate our database with the data from that file.

The `clients_data.json` file contains data for the models that we've created in the previous examples. If you want to create one of these files, you can use the `dumpdata` command to create a JSON file from your database:
```bash
python manage.py dumpdata clients > clients_data.json
```
Note you can use the `--indent 2` option to make the JSON file more readable:
```bash
python manage.py dumpdata clients --indent 2 > clients_data.json
```

This is a useful command to create a backup of your database or to share data with others.

### 2. Let's create a few views with our models.
So far in views we haven't fetched specific from the database we've just listed all of the objects in the database. Now we will create views that will fetch specific objects from the database.

Copy company detail `company_detail.html` template from the `templates` directory to your app's `templates/clients` directory.

Open the `views.py` file in your app directory and add the following code:

```python
from django.shortcuts import render, get_object_or_404

from .models import Company

# ... list_companies view ...


def company_detail(request, company_id):
    # fetching a specific company by its ID or returning a 404 error if not found
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'clients/company_detail.html', {'company': company})

```

Let's update the `urls.py` file in your app directory to include the new view:

```python
from django.urls import path
from .views import list_companies, company_detail

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    path('company/<int:company_id>/', company_detail, name='company_detail'),
]

```
This will make a view that we can access the company detail page by going to `/company/<company_id>/` in our browser.
- Next we're going to use our knowledge of the orm get the data

### 3. Let's add some data  to the template, using the `company` object we fetched in the view.
Open the `company_detail.html` template in your app's `templates/clients` directory and add the following code:

```html
{% extends "base.html" %}

{% block content %}

<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold underline">
        <!-- title here-->
        {{ company.name }}
    </h1>
    <!-- Information about the company below -->
    <section>
        <h2 class="text-2xl font-semibold mt-4">
            <!-- subtitle here -->
            About {{ company.name }}
        </h2>
        <p class="text-gray-700">
            <!-- description here -->
            {{company.description}}
        </p>
    </section>
</div>

{% endblock %}
```
You can see that we can use the company object from the database to display the company's name and description in the template.

Let's also list all of the employees that work for this company. We can do this by using the `related_name` we set in the `Employee` model.
```html

<section class="mt-6">
    <h2 class="text-2xl font-semibold">Employees</h2>
    <ul class="list-disc pl-5">
        <!-- Loop through the employees in the company -->
        {% for employee in company.employees.all %}
            <li>
                <!-- Display the name -->
                {{ employee.first_name }} {{ employee.last_name }}
                <!-- Display the role of the employee-->
                {% if employee.role %}
                <span class="text-gray-600 font-bold">({{ employee.role }})</span>
                {% else %}
                <span class="text-gray-600 font-bold">(role unknown)</span>
                {%endif %}

                <!-- Display the email -->
                <span class="text-gray-500">({{ employee.email }})</span>

            </li>
        {% empty %}
            <li>No employees found.</li>
        {% endfor %}
    </ul>
</section>
```
Let's breakdown what this does:
- We loop through all of the employees that are related to the company using `company.employees.all` (we don't use the () in the jinja template to call the method).
- We first display the employee's first name and last name. with `{{ employee.first_name }} {{ employee.last_name }}`.
- Next, we check if the employee has a role using `{% if employee.role %}`. If they do, we display their role in parentheses. If they don't have a role, we display "(role unknown)".
- Finally, we display the employee's email address in parentheses using `{{ employee.email }}`.

### 4. Let's add another company using the `loaddata` command so we can do a bit more filtering.

We have a company called "Quantum Solutions" in the the `clients_data_quantum.json` file. Let's load this data into our database using the `loaddata` command:
```bash
python manage.py loaddata clients_data_quantum.json
```

You can access this new company by going to the URL:
`http://localhost:8000/clients/company/10/`


### 5. Let's add a `employees_search_results` view to search for the employees by their first name

Open the `views.py` file in your app directory and add the following code:

```python
# Create your views here.
from .models import Company, Employee

# ... existing views ...

def employees_search_results(request, company_id):
    # this is going to handle the search query for employees
    query = request.GET.get('q', '')
    company = get_object_or_404(Company, id=company_id)

    if query:
        # If a query is provided, filter employees by first name
        # using icontains for case-insensitive search
        # company.employees is a queryset of employees related to the company
         # and we filter it by first_name__icontains=query
         # this will return all employees whose first name contains the query string
        employees = company.employees.filter(
            first_name__icontains=query
         )
    else:
        # If no query is provided, return an empty queryset
        employees = Employee.objects.none()
    # return
    return render(request, 'clients/employees_search_results.html', {'employees': employees, 'query': query})
```
Let's break down what this does:
- we get the search query from the request using `request.GET.get('q', '')`. If no query is provided, it defaults to an empty string.
- If a query is provided, we filter the employees of the company by their first name using `first_name__icontains=query`. This allows for case-insensitive searching.
  - *In SQL, this would translate to a query like `SELECT * FROM employees WHERE first_name LIKE '%query%'`*.
  - Note that There are other filters we can use such as `__exact`, `__iexact`, `__contains`, `__icontains`, `__gt`, `__gte`, `__lt`, `__lte`, and `__in` to filter the data in different ways. Here's a link to the [Django documentation on field lookups](https://docs.djangoproject.com/en/stable/ref/models/querysets/#field-lookups) for more details. Note we'll be using more of these in the future.
- If no query is provided, we return an empty queryset using `Employee.objects.none()`.
  - This is useful to avoid returning all employees when no search term is provided.

Let's update the `urls.py` file in your app directory to include the new view:

```python
from django.urls import path
from .views import list_companies, company_detail, employees_search_results
urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    path('company/<int:company_id>/', company_detail, name='company_detail'),
    path('company/<int:company_id>/employees/results/', employees_search_results, name='employees_search_results'),
]
```

Let's update the `employees_search_results.html` template in your app's `templates/clients` directory to display the search results:

```html
{% extends 'base.html' %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold underline">
        <!-- title here-->
        Employees of {{ company.name }}
    </h1>
    <div class="text-lg">search query: {{query}} </div>
    <section>
        <ul class="list-disc pl-5">
            {% for employee in employees %}
                <li class="mb-2">
                    <strong>{{ employee.first_name }} {{ employee.last_name }}</strong>
                    <div>
                        {{ employee.email }}
                    </div>
                    <p>Role: {{employee.role}}</p>

                </li>
            {% endfor %}
        </ul>
</div>

{% endblock %}
```
Now to test this out, you can go to the URL:
- `http://localhost:8000/clients/company/10/employees/results/?q=ma` which should return two results: "Mason Lee" and "Emma Martinez".
`http://localhost:8000/clients/company/10/employees/results/?q=liam` which should return one result: "Liam Nguyen"

### 6. Let's expand the `employees_search_results` view to search for employees by their last name as well.
In django there's a special `Q` object that allows us to create complex queries with OR and AND conditions. We can use this to search for employees by their first name or last name.

```python
# the Q object allows us to create complex queries with OR and AND conditions
from django.db.models import Q

# ... existing imports ...

# ... existing views ...

def employees_search_results(request, company_id):
    query = request.GET.get('q', '')
    company = get_object_or_404(Company, id=company_id)
    if query:
        # Using Q objects to search by first name or last name
        employees = Employee.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
    else:
        employees = Employee.objects.none()

    return render(request, 'clients/employees_search_results.html', {'employees': employees, 'query': query, 'company': company})
```
Let's break down what this does:
- We import the `Q` object from `django.db.models`.
- We use the `Q` object to create a query that searches for employees by their first name or last name using the `|` operator for OR conditions.
- *In SQL, this would translate to a query like `SELECT * FROM employees WHERE first_name LIKE '%query%' OR last_name LIKE '%query%'`*.

Now if you test this url:
- `http://localhost:8000/clients/company/10/employees/results/?q=ar` you should see the resutls for "Gary Smith", "Olvia Garcia", "Ethan Clark" and "Emma Martinez".

## Challenge/Exercise

Create a view for Roles that will allow you to search for employees by their role. You can use the same approach as the `employees_search_results` view, but filter by the `role` field instead.

## Conclusion
In this example, we learned how to:
- Load data into a fresh database using the `loaddata` command.
- Create views to fetch specific objects from the database using `get_object_or_404`.
- Use the `Q` object to create complex queries with OR and AND conditions.
- Filter employees by their first name or last name in a search view.
- Get a deeper understanding of how to use ORM results in a jinja template.

Next we'll be creating forms to allow users to update data in our database while we validate and santize the input before saving it to the database. This will help us ensure that the data we store is valid, consistent and safe.