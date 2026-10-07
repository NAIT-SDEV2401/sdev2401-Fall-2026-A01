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

acme = Company.objects.get(name="Acme Inc.")
print(f"{acme.name} founded on {acme.created_at}")
employees = Employee.objects.filter(company=acme)

# exercise: loop through the employees and print out all the fields