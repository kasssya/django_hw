from django.urls import path
from . import views

app_name = "parser"
urlpatterns = [
    path("parser/", views.ParserFormView.as_view(), name="parser"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/<int:id>/", views.BookDetailView.as_view(), name="book_list")

]