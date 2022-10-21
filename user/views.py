from django.shortcuts import render
from .models import *
from authentication.models import *

def userCart(request):

    if request.user.is_authenticated:
        customer = UserDetails.objects.get(customer=request.user.id)    
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []

    cart_total = 0
    for item in items:
        price = int(item.product.price.replace(',',''))
        cart_total += price * item.quantity
    cart_total = str(cart_total)
    
    
    context = {'items':items, 'total':cart_total}
    return render(request, 'shopping-cart.html', context) 