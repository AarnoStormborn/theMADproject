from django.urls import path
from . import views 

urlpatterns = [
    path('usercart', views.userCart, name='userCart')
]