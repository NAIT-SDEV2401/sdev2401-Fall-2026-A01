from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def register(request):
    # STUDENT TODO:
    # handle the request.method if it's a "POST"
    # check if the form is valid by passing in the request.POST to the form.
    # redirect to login page after successful registration

    # this will be the default
    return render(
        request,
        "core/register.html",
        {
            "form": UserCreationForm(),
        },
    )
