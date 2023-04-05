from rest_framework import serializers

from library.models import Book, Author, User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# class ReaderSerializer(serializers.ModelSerializer):
#
#     def validate(self, data):
#         self.__validate_count_books(data.get('books'))
#         return super().validate(data)
#
#     @staticmethod
#     def __validate_count_books(books: dict):
#         if len(books) > 3:
#             raise ValidationError('Max count books 3')
