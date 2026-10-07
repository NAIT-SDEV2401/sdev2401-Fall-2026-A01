# region environment set up
#!/usr/bin/env python
### ! Do not edit ! ###
import os
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()
print("Django environment set up successfully.")
# endregion


from clients.models import Employee, Company

# 1. objects.all() and objects.filter - BOTH RETURN QUERYSETS
    # companies = Company.objects.all()
    # print(companies)
    # print(companies[0])
    # print(companies[1])
    # companies = Company.objects.filter(name="Acme Inc.")
    # if(companies):
    #     print(companies)
    # else:
    #     print("no companies to display")

#2. objects.get, filtering by passing a model, and looping through a queryset
    # acme = Company.objects.get(name="Acme Inc.")
    # print(f"{acme.name} founded on {acme.created_at}")
    # employees = Employee.objects.filter(company=acme)

    # # exercise: loop through the employees and print out all the fields
    # for e in employees:
    #     print(f"{e.first_name} {e.last_name} was hired by {e.company} on {e.created_at:%Y-%m-%d}")

# 3. two ways to insert data into the database
new_employees_data_acme = [
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@acmetesting.com",
        "company": "Acme",
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@acmetesting.com",
        "company": "Acme",
    },
    {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@acmetesting.com",
        "company": "Acme",
    },

]
# for the second part.
new_employees_data_cat_sitting_int = [
    {
        "first_name": "Diana",
        "last_name": "Prince",
        "email": "diana.prince@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "CEO",
    },
    {
        "first_name": "Ethan",
        "last_name": "Hunt",
        "email": "ethan.hunt@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Manager",
    },
    {
        "first_name": "Fiona",
        "last_name": "Green",
        "email": "fiona.green@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Developer",
    },
]

acme_company = Company.objects.get(name="Acme Inc.")
e_data = new_employees_data_acme[1]

# new_employee = Employee(
#     first_name=e_data['first_name'],
#     last_name=e_data['last_name'],
#     email=e_data['email'],
#     company=acme_company
# )
# new_employee.save()

new_employee = Employee.objects.create(
    first_name=e_data['first_name'],
    last_name=e_data['last_name'],
    email=e_data['email'],
    company=acme_company
)