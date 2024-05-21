from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from .forms import SearchForm

def index(request):
    return render(request, 'catalog/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'catalog/author_list.html', {'authors': authors})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'catalog/author_detail.html', {'author': author})

def search(request):
    form = SearchForm()
    query = request.GET.get('query')
    books = []
    authors = []

    if query:
        books = Book.objects.filter(title__icontains=query)
        authors = Author.objects.filter(first_name__icontains=query) | Author.objects.filter(last_name__icontains=query)

    return render(request, 'catalog/search_results.html', {'form': form, 'books': books, 'authors': authors})