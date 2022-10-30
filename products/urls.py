from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    path('searchProducts', views.searchProducts, name='searchProducts')
]