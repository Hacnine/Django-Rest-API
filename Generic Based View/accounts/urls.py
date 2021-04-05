from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentList.as_view()),
    # path('<int:pk>/', views.StudentList.as_view()),
    path('create/<int:pk>/', views.StudentCRUD.as_view()),
    # path('retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('update/<int:pk>/', views.StudentUpdate.as_view()),
    # path('delete/<int:pk>/', views.StudentDestroy.as_view()),

]
