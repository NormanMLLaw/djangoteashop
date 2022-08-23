from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")


def shop(request):
    return render(request, "pages/shop.html")


def contact(request):
    return render(request, "pages/contact.html")


def login_register(request):
    return render(request, "pages/login_register.html")


    