from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    num_pages = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = PhoneNumberField(blank=True)
    is_active = models.BooleanField(default=True)
    books = models.ManyToManyField(Book, max_length=3)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return f"{self.name} {self.surname}"


