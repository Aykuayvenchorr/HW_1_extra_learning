from rest_framework import serializers
from django.core.exceptions import ValidationError


def phone_validator(value):
    if len(str(value)[1::]) != 11:
        raise ValidationError("В номере должно быть 11 цифр")
    if str(value)[1] != '7':
        raise ValidationError("Номер должен начинаться с 7")


def book_validator(value):
    if value < 1:
        raise ValidationError("Количество страниц не может быть отрицательным")


class ReaderSerializer(serializers.ModelSerializer):

    def validate(self, data):
        self.__validate_count_books(data.get('books'))
        return super().validate(data)

    @staticmethod
    def __validate_count_books(books: dict):
        if len(books) > 3:
            raise ValidationError('Max count books 3')
