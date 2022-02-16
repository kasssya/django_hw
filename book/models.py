from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title




class BookFeedback(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
