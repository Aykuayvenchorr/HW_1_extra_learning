from rest_framework import viewsets

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from library.models import Book, Author, Reader
from library.serializers import BookSerializer, AuthorSerializer, ReaderSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [IsAdminUser]


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [IsAdminUser()]


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [IsAdminUser()]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    default_permission = [AllowAny()]

    permissions = {
        'list': [AllowAny()],
        'create': [IsAdminUser()],
        'update': [IsAdminUser()],
        'destroy': [IsAdminUser()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    default_permission = [IsAdminUser(), IsAuthenticated()]

    permissions = {
        'create': [AllowAny()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)