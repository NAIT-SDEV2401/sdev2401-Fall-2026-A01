from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import 

# Create your views here.
def home(request):
    return render(request, "trails/home.html")


@login_required
def briefing(request):
    return render(request, "trails/briefing.html")
