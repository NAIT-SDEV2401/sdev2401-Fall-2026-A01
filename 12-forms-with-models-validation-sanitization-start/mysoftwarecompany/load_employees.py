import os
import django

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysoftwarecompany.settings')
django.setup()

# Note place your imports below and do not remove the above lines
##### YOUR CODE BELOW THIS LINE #####


from clients.models import Employee, Company, Role

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
def main():

    for employee_data in new_employees_data_cat_sitting_int:
        # Get or create the company
        company, created = Company.objects.get_or_create(name=employee_data["company"])

        # Get or create the role
        role, created = Role.objects.get_or_create(name=employee_data["role"])

        # Create the employee
        employee, created = Employee.objects.get_or_create(
            first_name=employee_data["first_name"],
            last_name=employee_data["last_name"],
            email=employee_data["email"],
            company=company,
            role=role,
        )
        if created:
            # If the employee was created, print a message
            print(f"Created new employee: {employee}")
        else:
            # If the employee already exists, print a message
            print(f"Employee: {employee} already exists, skipping creation.")


if __name__ == "__main__":
    main()
    print("All employees have been processed.")