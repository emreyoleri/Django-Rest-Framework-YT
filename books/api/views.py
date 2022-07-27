from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        book_pk = self.kwargs.get("book_pk")
        book = get_object_or_404(Book, pk=book_pk)
        return serializer.save(book=book)


class CommentDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


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
