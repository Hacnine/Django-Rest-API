from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Student
from .serializers import StudentSerializer


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



