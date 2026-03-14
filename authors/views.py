from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorCreateForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorCreateForm()
    return render(request, 'authors/author_form.html', {'form': form, 'title': 'Create Author'})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})