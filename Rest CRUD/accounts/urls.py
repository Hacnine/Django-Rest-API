from django.urls import path

from . import views

urlpatterns = [
    path('', views.student, name='store'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout')
]
