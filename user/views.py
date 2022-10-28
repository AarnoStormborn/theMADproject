from django.shortcuts import render
from .models import *
from authentication.models import *

def userCart(request):

    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)    
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
    
    context = {'items':items, 'order':order}
    return render(request, 'shopping-cart.html', context) 

def checkout(request):

    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)    
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
    
    context = {'items':items, 'order':order}
    return render(request, 'checkout.html', context)