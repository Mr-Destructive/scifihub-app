from django.shortcuts import get_object_or_404, redirect, render

from scifihub.core.middlewares import author_access_required

from .forms import BookForm, ChapterForm, ChapterEditForm
from .models import Book, Chapter


@author_access_required
def book_list(request):
    user = request.user
    books = Book.objects.filter(author=user)
    return render(request, "books/list.html", {"books": books})


@author_access_required
def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
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


def book_edit(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:list")
    return render(request, "books/edit.html", {"book": book, "form": form})


def book_delete(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    if request.method == "POST":
        book.delete()
        return redirect("books:list")
    return render(request, "books/delete.html", {"book": book})


def add_chapter(request, book_slug):
    book = Book.objects.get(slug=book_slug)
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
    return render(request, "books/chapter.html", {"chapter": chapter, "book": book})


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
        return render(request, "books/chapter.html", {"chapter": chapter, "book": book})
    return render(
        request,
        "books/chapters/delete-chapter.html",
        {"chapter": chapter, "book": book},
    )


def chapeter_write(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    form = ChapterEditForm(instance=chapter)
    if request.method == "PATCH":
        form = ChapterEditForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("books:chapter", book_slug, chp_slug)
    return render(
        request,
        "books/chapters/write.html",
        {"form": form, "chapter": chapter, "book": book},
    )
