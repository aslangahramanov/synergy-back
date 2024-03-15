from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/<int:pk>/<str:slug>', views.product_detail, name='product-detail'),
]
