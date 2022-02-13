from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.books_all, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
]