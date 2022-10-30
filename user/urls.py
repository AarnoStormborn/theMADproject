from django.urls import path
from . import views 

urlpatterns = [
    path('usercart', views.userCart, name='userCart'),
    path('checkout', views.checkout, name='checkout'),
    path('updatecart', views.updateCart, name='updatecart')
]