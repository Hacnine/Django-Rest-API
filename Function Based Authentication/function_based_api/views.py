from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view()
# def mellow_world(request):
#     return Response({'msg': 'Mellow world'})


# @api_view(['GET'])
# def mellow_world(request):
#     return Response({'msg': 'Mellow world'})


@api_view(['GET', 'POST'])
def mellow_world(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg': 'Its a get request'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'Its a post request', 'data': request.data})


def cart(request):

    context = {}
    return render(request, 'cart.html', context)


def checkout(request):

    context = {}
    return render(request, 'checkout.html', context)


