from rest_framework import serializers

from library.models import Book, Author, Reader


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = '__all__'

