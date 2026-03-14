from django.db import models
from authors.models import Author
from categories.models import Category

class Book(models.Model):

    title = models.CharField(max_length=150)

    description = models.TextField()

    published_year = models.IntegerField()

    pages = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    categories = models.ManyToManyField(
        Category,
        related_name="books"
    )

    def __str__(self):
        return self.title
