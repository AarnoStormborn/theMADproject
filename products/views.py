from django.shortcuts import render
from .models import Mobile
from user.models import *

def products(request):
    data = Mobile.objects.all()
    context = {'data':data}
    return render(request, 'products/products.html', context)

def product(request, id):

    data = Mobile.objects.get(id=id)
    context = {'mobile':data}
    return render(request, 'products/product.html', context)