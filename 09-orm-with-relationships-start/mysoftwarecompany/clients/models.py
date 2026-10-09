from django.db import models


# our model for the client
class Company(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # company description
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    # core fields
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)  # optional field

    # We're going to be adding these quite commonly.
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    # core fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')
    def __str__(self):
        # note that you can use self.company to access the str representation of the related Company instance
        return f"{self.first_name} {self.last_name} works at {self.company.name}"