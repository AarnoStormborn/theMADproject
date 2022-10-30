from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from authentication.models import *
from products.models import *

def userCart(request):

    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)    
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
    
    context = {'items':items, 'order':order}
    return render(request, 'user/shopping-cart.html', context) 

def checkout(request):

    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)    
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
    
    context = {'items':items, 'order':order}
    return render(request, 'user/checkout.html', context)

@csrf_exempt
def updateCart(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        customer = Profile.objects.get(user=request.user)  
        product = Mobile.objects.get(id=productId)  
        order, created = Order.objects.get_or_create(customer=customer)
        
        orderItem, created = OrderItem.objects.get_or_create(product=product,order=order)
        
        responseMessage = {}
        if action=='add':
            orderItem.quantity = (orderItem.quantity + 1)
            responseMessage["Message"] = "Item added to Cart"
        if action=='remove':
            orderItem.quantity = (orderItem.quantity - 1)
            responseMessage["Message"] = ""
        if action=='removeAll':
            orderItem.quantity = 0
            responseMessage["Message"] = "Item Removed"


        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()
        
        return JsonResponse(responseMessage, status=200)
    return JsonResponse({}, status=400)