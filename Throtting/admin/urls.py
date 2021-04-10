from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from accounts.views import *

router = DefaultRouter()
router.register('myapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),

    # path('api/', StudentList.as_view()),
    # path('api/<int:pk>', StudentCreate.as_view()),
    # path('api/<int:pk>', StudentRetrieve.as_view()),
    path('api/<int:pk>', StudentUpdate.as_view()),

]
