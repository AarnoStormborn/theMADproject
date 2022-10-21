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

    cart_total = 0
    for item in items:
        price = int(item.product.price.replace(',',''))
        cart_total += price * item.quantity
    cart_total = str(cart_total)

    cart_total = cart_total[::-1]
    total = [cart_total[i:i+3] for i in range(0, len(cart_total), 3)]
    final_amt = ''
    for i in total:
        final_amt += i + ','
    final_amt = final_amt[::-1]
    final_amt = final_amt[1:]
    print(final_amt)
    
    context = {'items':items, 'total':final_amt}
    return render(request, 'shopping-cart.html', context) 