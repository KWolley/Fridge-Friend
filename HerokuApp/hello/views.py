from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.

def recipes(request):
    # link recipes.html page in from base.html
    return render(request, "recipes.html")

def pantry(request):
    return render(request, "pantry.html")

def main(request):
    return render(request, "main.html")
