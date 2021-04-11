from django.contrib import admin
from django.urls import path, include
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', StudentList.as_view()),
]
