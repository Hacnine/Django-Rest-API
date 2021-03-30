from django.urls import path

from . import views

urlpatterns = [
    path('', views.mellow_world, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
