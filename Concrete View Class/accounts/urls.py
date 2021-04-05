from django.urls import path

from . import views

urlpatterns = [
    # path('', views.StudentList.as_view()),
    # path('<int:pk>/', views.StudentList.as_view()),
    # path('create/', views.StudentCreate.as_view()),

    # path('retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('update/<int:pk>/', views.StudentUpdate.as_view()),
    # path('delete/<int:pk>/', views.StudentDestroy.as_view()),

    path('list-create/', views.StudentListCreate.as_view()),
    # path('retrieve-update/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    # path('retrieve-destroy/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('retrieve-update-destroy/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),

]
