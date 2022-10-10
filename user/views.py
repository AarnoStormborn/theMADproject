from django.shortcuts import render

def userCart(request):
    return render(request, 'shopping-cart.html')