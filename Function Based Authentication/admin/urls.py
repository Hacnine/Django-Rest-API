from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from function_based_CRUD_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('function_based_api.urls')),
    path('crud/', views.student_api),
    path('crud_browse/', views.browsable_student_api),
    path('crud_browse/<int:pk>/', views.browsable_student_api),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
#
#     # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
