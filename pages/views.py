from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")


def shop(request):
    return render(request, "pages/shop.html")


def contact(request):
    return render(request, "pages/contact.html")


def login_register(request):
    return render(request, "pages/login_register.html")


    