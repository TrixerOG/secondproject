from django.shortcuts import render
from .models import Book, Author


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    return render(request, 'index.html', context={'num_books': num_books, 'num_authors': num_authors})


def book_list(request):
    sort_by = request.GET.get('sort_by', 'title')
    direction = request.GET.get('direction', 'asc')
    if direction == 'desc':
        sort_by = f'-{sort_by}'

    books = Book.objects.all().order_by(sort_by)

    new_direction = 'desc' if direction == 'asc' else 'asc'

    return render(request, 'book_list.html', {'books': books, 'new_direction': new_direction})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_detail.html', {'author': author})