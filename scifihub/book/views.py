from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm, ChapterForm

from .models import Book, Chapter


def book_list(request):
    user = request.user
    books = Book.objects.filter(author=user)
    return render(request, "books/list.html", {"books": books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    chapters = book.chapters.all()
    return render(request, "books/detail.html", {"book": book, "chapters": chapters})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books:list")
        else:
            return render(request, "books/create.html", {"form": form})
    return render(request, "books/create.html")


def book_edit(request, slug):
    book = Book.objects.get(slug=slug)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:list")
    return render(request, "books/edit.html", {"book": book, "form": form})


def book_delete(request, slug):
    book = Book.objects.get(slug=slug)
    if request.method == "POST":
        book.delete()
        return redirect("books:list")
    return render(request, "books/delete.html", {"book": book})


def add_chapter(request, slug):
    book = Book.objects.get(slug=slug)
    form = ChapterForm()
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            chapter.book = book
            chapter.save()
            return render(request, "books/chapter.html", {"chapter": chapter})
    return render(
        request, "books/chapters/create-chapter.html", {"form": form, "book": book}
    )


def chapter_detail(request, book_slug, chp_slug):
    book = Book.objects.get(slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    return render(request, "books/chapter.html", {"chapter": chapter})

def chapter_edit(request, book_slug, chp_slug):
    book = Book.objects.get(slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    if request.method == "POST":
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return render(request, "books/chapter.html", {"chapter": chapter})
    return render(
        request, "books/chapters/edit-chapter.html", {"form": form, "book": book}
    )

def chapter_delete(request, book_slug, chp_slug):
    book = Book.objects.get(slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    if request.method == "POST":
        chapter.delete()
        return render(request, "books/chapter.html", {"chapter": chapter})
    return render(request, "books/chapters/delete-chapter.html", {"chapter": chapter})

