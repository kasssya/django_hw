from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

def books_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {'book': book})

def book_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html",{"books": books} )