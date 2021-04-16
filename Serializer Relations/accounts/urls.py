from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views


router = DefaultRouter()
router.register('author', views.AuthorViewSet, basename='author')
router.register('book', views.BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

