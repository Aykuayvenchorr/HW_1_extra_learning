from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PhoneValidator:
    def __call__(self, value):
        if len(str(value)[1::]) != 11:
            raise serializers.ValidationError("В номере должно быть 11 цифр")
        if str(value)[1] != '7':
            raise serializers.ValidationError("Номер должен начинаться с 7")


class BookValidator:
    def __call__(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество страниц не может быть отрицательным")


class ReaderSerializer(serializers.ModelSerializer):

    def validate(self, data):
        self.__validate_count_books(data.get('books'))
        return super().validate(data)

    @staticmethod
    def __validate_count_books(books: dict):
        if len(books) > 3:
            raise ValidationError('Max count books 3')
