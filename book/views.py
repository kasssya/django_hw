from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from django.shortcuts import reverse, redirect


def books_all(request):
    book = models.Book.objects.filter().order_by("-id")
    return render(request, "book_list.html", {'book': book})

def book_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html",{"books": books} )

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("book:book_list"))
            # return HttpResponse("Книга удачно добавлена!")
    else:
        form = forms.BookForm()
    return  render (request, "add_book.html", {"form": form})
