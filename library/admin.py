from django.contrib import admin

from library.models import Author, Book, User

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)