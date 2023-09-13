from django.shortcuts import get_object_or_404, redirect, render
from book.forms import BookForm

from book.models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    chapters = book.chapters.all()
    print(chapters)
    return render(request, 'books/detail.html', {'book': book, 'chapters': chapters})

