from django.urls import path
from . import views


app_name = "book"
urlpatterns = [
    path('book/', views.BooksListView.as_view(), name='book_list'),
    path('book/<int:id>/', views.BooksDetailView.as_view(), name='book_detail'),
    path('book/<int:id>/update/', views.BooksUpdateView.as_view(), name='book_update'),
    path('book/<int:id>/delete/', views.BooksDeleteView.as_view(), name='book_delete'),
    path('add-book/', views.BooksAddView.as_view(), name='add_book'),

]