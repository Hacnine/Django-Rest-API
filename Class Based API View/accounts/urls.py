from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentAPI.as_view()),
    path('<int:pk>/', views.StudentAPI.as_view()),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
