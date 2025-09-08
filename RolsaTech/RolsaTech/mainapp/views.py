from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

def get_list_of_trending_products():
    pass

def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})
