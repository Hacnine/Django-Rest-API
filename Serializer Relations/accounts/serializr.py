from rest_framework import serializers

from accounts.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'page']


class AuthorSerializer(serializers.ModelSerializer):
    # ref_book = serializers.StringRelatedField(many=True, read_only=True)
    # ref_book = serializers.StringRelatedField(many=True, read_only=True)
    # ref_book = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')
    # ref_book = serializers.SlugRelatedField(many=True, read_only=True, slug_field='page')
    ref_book = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='book-detail')


    class Meta:
        model = Author
        fields = ['id', 'name', 'gender', 'ref_book']



