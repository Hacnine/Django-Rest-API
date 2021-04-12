from django.views.generic import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import *
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import *


# # One way to filter
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(passby=user)


# Another way to filter

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     # if you want to filter locally
#     filter_backends = [DjangoFilterBackend]
#     filter_fields = ['name', 'city']
#
#     # how to filter
#     #  http://127.0.0.1:8000/api/?name=Tanvir&city=Sylhe


# Search Filter

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     # if you want to filter locally
#     filter_backends = [SearchFilter]
#     # search_fields = ['city']
#
#     # how to filter
#     #  http://127.0.0.1:8000/api/?search=Sylhe
#     #  http://127.0.0.1:8000/api/?search=r
#
#     search_fields = ['^name']


# Ordering filter
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # if you want to filter locally
    filter_backends = [OrderingFilter]
    filter_fields = ['name', 'city']

    # how to filter
    #  http://127.0.0.1:8000/api/?name=Tanvir&city=Sylhe


