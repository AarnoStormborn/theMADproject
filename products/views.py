from django.shortcuts import render, redirect
from .models import Mobile
from user.models import *
from django.views.decorators.csrf import csrf_exempt

def products(request):
    data = Mobile.objects.all()
    context = {'data':data}
    return render(request, 'products/products.html', context)

def product(request, id):

    data = Mobile.objects.get(id=id)
    context = {'mobile':data}
    return render(request, 'products/product.html', context)


def searchProducts(request):
    
    if request.method == 'GET':
        
        qs = request.GET['query']
        data = Mobile.objects.filter(brand__icontains=qs)
        context = {'data':data}
        return render(request, 'products/products2.html', context)

    else: return redirect('products')