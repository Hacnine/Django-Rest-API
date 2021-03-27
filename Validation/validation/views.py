import io

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from validation.models import *
from validation.serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializr = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializr.data)
            return HttpResponse(json_data, content_type='application/json')

        else:
            stu = Student.objects.all()
            serializr = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializr.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializr = StudentSerializer(data=python_data)

        if serializr.is_valid():
            serializr.save()
            response = {'msg': 'Data inserted.'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializr.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializr = StudentSerializer(stu, data=python_data,
                                      partial=True)

        if serializr.is_valid():
            serializr.save()
            response = {'msg': 'Data updated.'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        # else:
        json_data = JSONRenderer().render(serializr.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()

        response = {'msg': 'Data deleted.'}
        return JsonResponse(response, safe=False)



