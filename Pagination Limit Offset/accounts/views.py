from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Student
from .my_pagination import MyPagination
from .serializers import StudentSerializer


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination



