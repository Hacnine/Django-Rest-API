from datetime import datetime, timedelta
import stripe
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Student
from accounts.serializers import StudentSerializer


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        get_id = pk
        if get_id is not None:
            students = Student.objects.get(id=get_id)
            serializer = StudentSerializer(students)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        print('serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        get_id = pk
        student = Student.objects.get(id=get_id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        get_id = pk
        student = Student.objects.get(id=get_id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})

        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        get_id = pk
        student = Student.objects.get(id=get_id)
        student.delete()
        return Response({'msg': 'Data Deleted.'})


def cart(request):

    context = {}
    return render(request, 'cart.html', context)


def checkout(request):

    context = {}
    return render(request, 'checkout.html', context)


