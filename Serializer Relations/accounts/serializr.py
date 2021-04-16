from rest_framework import serializers

from accounts.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'page']


class AuthorSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        # fields = ['id', 'name', 'gender', 'ref_book']
        fields = ['id', 'name', 'gender']



