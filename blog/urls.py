from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('article/<int:pk>/<str:slug>/', views.article, name='article'),
]
