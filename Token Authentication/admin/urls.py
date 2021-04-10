from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from accounts import views
from accounts.auth import CustomAuthToken

router = DefaultRouter()
router.register('myapi', views.StudentModelViewSet, basename='student')

router2 = DefaultRouter()
router2.register('myapi2', views.CustomAuth, basename='custom')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),
    # Commands: http post http://127.0.0.1:8000/gettoken/ username="admin" password="1"

    path('as/', include(router2.urls)),
    path('auth2/', include('rest_framework.urls',
                           namespace='rest_framework')),
    path('getcustom/', CustomAuthToken.as_view())
]
