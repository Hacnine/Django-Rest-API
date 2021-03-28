from django.contrib import admin
from model_serializer.models import *

admin.site.register(Student)
# admin.site.register(CourseModule)
# admin.site.register(Profile)

# from .models import Page
#
#
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']