from django.shortcuts import get_object_or_404, redirect, render

from scifihub.core.middlewares import author_access_required
from scifihub.projects.models import Project

from .forms import BookForm, ChapterForm, ChapterWriteForm
from .models import Book, Chapter


@author_access_required
def book_list(request):
    user = request.user
    books = Book.objects.filter(author=user)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "books/fragments/list.html", {"books": books})
    return render(request, "books/list.html", {"books": books})


@author_access_required
def project_books(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    books = Book.objects.filter(project=project)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "books/fragments/list.html", {"books": books}) 
    return render(request, "books/list.html", {"books": books})


@author_access_required
def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapters = book.chapters.all()
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "books/fragments/detail.html", {"book": book, "chapters": chapters})
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
    book = get_object_or_404(Book, slug=book_slug)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:list")
    return render(request, "books/edit.html", {"book": book, "form": form})


def book_delete(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    if request.method == "POST":
        book.delete()
        return redirect("books:list")
    return render(request, "books/delete.html", {"book": book})


@author_access_required
def add_chapter(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    form = ChapterForm()
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            chapter.book = book
            chapter.save()
            return render(request, "books/chapters/detail.html", {"chapter": chapter})
    return render(
        request, "books/chapters/create.html", {"form": form, "book": book}
    )


def chapter_detail(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    return render(request, "books/chapters/detail.html", {"chapter": chapter, "book": book})


def chapter_edit(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    form = ChapterForm(instance=chapter)
    if request.META.get("HTTP_HX_REQUEST") and request.method == "POST":
        print("HERE")
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return render(request, "books/chapters/detail.html", {"book": book, "chapter": chapter})
    return render(
            request, "books/chapters/edit.html", {"form": form, "book": book, "chapter": chapter}
    )


def chapter_delete(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    if request.method == "POST":
        chapter.delete()
        chapters = book.chapters.all()
        return render(request, "books/detail.html", {"chapters": chapters, "book": book})
    return render(
        request,
        "books/chapters/delete.html",
        {"chapter": chapter, "book": book},
    )


def chapeter_write(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    form = ChapterWriteForm(instance=chapter)
    if request.META.get("HTTP_HX_REQUEST"):
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("books:chapter-detail", book_slug, chp_slug)
        else:
            return render(
                request,
                "books/chapters/detail.html",
                {"form": form, "chapter": chapter, "book": book},
            )
    return render(
        request,
        "books/chapters/write.html",
        {"form": form, "chapter": chapter, "book": book},
    )

def word_count_chapter(chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return len(chapter.text_content)
