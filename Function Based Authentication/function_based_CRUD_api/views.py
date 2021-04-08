import io

from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from function_based_CRUD_api.models import *
from function_based_CRUD_api.serializers import StudentSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request):

    if request.method == 'GET':
        get_id = request.data.get('id')
        if get_id is not None:
            students = Student.objects.get(id=get_id)
            serializer = StudentSerializer(students)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        print('request.data', request.data)
        serializer = StudentSerializer(data=request.data)
        print('serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        get_id = request.data.get('id')
        student = Student.objects.get(id=get_id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})

        return Response(serializer.errors)

    if request.method == 'DELETE':
        get_id = request.data.get('id')
        student = Student.objects.get(id=get_id)
        student.delete()
        return Response({'msg': 'Data Deleted.'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def browsable_student_api(request, pk=None):
    if request.method == 'GET':
        get_id = pk
        if get_id is not None:
            students = Student.objects.get(id=get_id)
            serializer = StudentSerializer(students)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        print('request.data', request.data)
        serializer = StudentSerializer(data=request.data)
        print('serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == 'PUT':
        get_id = pk
        student = Student.objects.get(id=get_id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    if request.method == 'PATCH':
        get_id = pk
        student = Student.objects.get(id=get_id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})

        return Response(serializer.errors)

    if request.method == 'DELETE':
        get_id = pk
        student = Student.objects.get(id=get_id)
        student.delete()
        return Response({'msg': 'Data Deleted.'})




