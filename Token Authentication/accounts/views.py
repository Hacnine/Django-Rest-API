from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from .models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]    # For this command: http http://127.0.0.1:8000/myapi/

    # Commands-GET: http http://127.0.0.1:8000/myapi/ "Authorization:Token 8a467d1606d48e64ca812ba47bdd471c23907798"
    # Commands-POST: http -f POST  http://127.0.0.1:8000/myapi/ name=Yasin roll=14 city=Dhaka "Authorization:Token 8a467d1606d48e64ca812ba47bdd471c23907798" Tutorial: Token Authentication
    # Commands-PUT: http -f PUT  http://127.0.0.1:8000/myapi/3/ name=Abir roll=14 city=Dhaka "Authorization:Token 8a467d1606d48e64ca812ba47bdd471c23907798"
    # Commands-DELETE: http DELETE  http://127.0.0.1:8000/myapi/3/ "Authorization:Token 8a467d1606d48e64ca812ba47bdd471c23907798"


# For custom authentication
class CustomAuth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
