from django.urls import path

from .views import *

urlpatterns = [
    path('stu/<int:pk>', student_detail, name='home'),
    path('list_stu/', student_list, name=''),
    # path('/', checkout, name='')
]
