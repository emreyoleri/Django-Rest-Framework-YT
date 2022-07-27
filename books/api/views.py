from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book

# ? ConcreteViews
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ? ConcreteViews
class BookDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ? GenericAPIView
# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     # List

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Create

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
