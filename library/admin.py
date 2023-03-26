from django.contrib import admin
from django.contrib.admin import register
from django.db.models import QuerySet

from library.models import Author, Book, User


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(User)


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'photo')


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'quantity')
    list_display_links = ('author',)

    actions = ('change_quantity',)

    # метод для изменения наличия книг (установить значение 0)

    @admin.action(description='Изменение наличия книг. Установить 0')
    def change_quantity(self, request, queryset: QuerySet):
        queryset.update(quantity=0)
        self.message_user(request, f"Количество книг {queryset.values('quantity')}")


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone_number', 'is_active', 'get_books')
    list_filter = ('is_active',)

    actions = ('change_status', 'delete_books')

    def get_books(self, obj):
        return [book.title for book in obj.books.all()]

    get_books.short_description = 'Books'

    def save_model(self, request, obj, form, change):
        if len(form.cleaned_data["books"]) > 3:
            raise ValueError('Max only 3 books')
        else:
            list_books = []
            for book in form.cleaned_data["books"]:
                list_books.append(book)
                b = Book.objects.get(title=book.title)
                b.quantity -= 1
                b.save()

            self.message_user(request, f"{list_books}")
        return super().save_model(request, obj, form, change)

    # метод для изменения статуса активности читателя
    @admin.action(description='Обновить статус')
    def change_status(self, request, queryset: QuerySet):
        for el in queryset:
            if el.is_active:
                el.is_active = False
                el.save()
            else:
                el.is_active = True
                el.save()
            self.message_user(request, f'Статус {el.is_active}')

    # # метод для удаления всех книг у пользователя
    @admin.action(description='Удалить все книги у пользователя')
    def delete_books(self, request, queryset: QuerySet):
        for el in queryset:
            el.books.clear()
            self.message_user(request, f'{el.books}')
