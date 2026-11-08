from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "trails/home.html")


def briefing(request):
    return render(request, "trails/briefing.html")
