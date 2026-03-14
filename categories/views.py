from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryCreateForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryCreateForm()
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Create Category'})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/category_detail.html', {'category': category, 'books': category.books.all()})