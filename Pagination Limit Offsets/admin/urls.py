from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),

    path('api/', StudentList.as_view()),
    # path('api/<int:pk>', StudentCreate.as_view()),
    # path('api/<int:pk>', StudentRetrieve.as_view()),

]
