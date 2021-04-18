from rest_framework import serializers
from .models import Student


# Hyperlinked Model Serializer in Django REST Framework (Hindi)
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city']


