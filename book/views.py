from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from django.shortcuts import reverse, redirect
from django.views import generic

class BooksListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return self.queryset


# def books_all(request):
#     book = models.Book.objects.filter().order_by("-id")
#     return render(request, "book_list.html", {'book': book})
class BooksDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)



# def book_detail(request, id):
#     books = get_object_or_404(models.Book, id=id)
#     return render(request, "book_detail.html",{"books": books} )

class BooksAddView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksAddView, self).form_valid(form=form)

# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book:book_list"))
#             # return HttpResponse("Книга удачно добавлена!")
#     else:
#         form = forms.BookForm()
#     return  render (request, "add_book.html", {"form": form})

class BooksUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/book/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpdateView, self).form_valid(form=form)

#
# def put_book_update(request,id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_id,
#                               data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book:book_list"))
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, "book_update.html",{"form": form,
#                                                "book": book_id})


class BooksDeleteView(generic.DeleteView):
    success_url = "/book/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)


# def book_delete(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     # return HttpResponse("Show Deleted")
#     return redirect(reverse("book:book_list"))