from django.shortcuts import render
from books.models import Book
from authors.models import Author
from categories.models import Category

def home(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'home.html', context)