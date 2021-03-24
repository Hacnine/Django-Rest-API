from django.urls import path

from .views import *

urlpatterns = [
    path('', student_create, name='home'),
    # path('list_stu/', student_list, name=''),
    # path('/', checkout, name='')
]
