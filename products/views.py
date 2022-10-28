from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Mobile

def products(request):
    data = Mobile.objects.all()
    context = {'data':data}
    return render(request, 'products/products.html', context)

def product(request, id):

    data = Mobile.objects.get(id=id)
    context = {'mobile':data}
    return render(request, 'products/product.html', context)

@csrf_exempt
def updateCart(request):
    return JsonResponse("Item Was Added")