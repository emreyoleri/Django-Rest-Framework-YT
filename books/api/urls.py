from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path("books/", api_views.BookListCreateAPIView.as_view(), name="book-list"),
    path("books/<int:pk>",
         api_views.BookDetailCreateAPIView.as_view(), name="book-detail"),
    path("books/<int:book_pk>/comment",
         api_views.CommentCreateAPIView.as_view(), name="comment"),
]
