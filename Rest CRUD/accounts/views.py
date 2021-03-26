import io

from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from accounts.models import *
from accounts.serializers import StudentSerializer


def student(request):

    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializr = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializr.data)
            return HttpResponse(json_data, content_type='application/json')

    stu = Student.objects.all()
    serializr = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializr.data)
    return HttpResponse(json_data, content_type='application/json')

