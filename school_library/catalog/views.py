from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context)


def book_list(request):
    sort_by = request.GET.get('sort_by', 'title')
    direction = request.GET.get('direction', 'asc')

    if direction == 'desc':
        sort_by = '-' + sort_by

    books = Book.objects.all().order_by(sort_by)

    # Determine the new direction for the next click
    new_direction = 'desc' if direction == 'asc' else 'asc'

    context = {
        'books': books,
        'sort_by': sort_by.lstrip('-'),
        'direction': direction,
        'new_direction': new_direction,
    }

    return render(request, 'book_list.html', context)

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author_detail.html', context)