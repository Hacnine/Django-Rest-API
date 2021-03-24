from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from .models import *
from django.shortcuts import render

from .models import *
from .serializers import StudentSerializer


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print('stu', stu)

    serializer = StudentSerializer(stu)
    # print('serializer', serializer)

    json_data = JSONRenderer().render(serializer.data)
    # print('json_data', json_data)

    context = {}
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    print('stu', stu)

    serializer = StudentSerializer(stu, many=True)
    print('serializer', serializer)

    # json_data = JSONRenderer().render(serializer.data)
    # print('json_data', json_data)

    context = {}
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
