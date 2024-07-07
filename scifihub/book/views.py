from slugify import slugify
from django.shortcuts import get_object_or_404, redirect, render

from scifihub.core.middlewares import author_access_required
from scifihub.projects.models import Project

from .forms import BookForm, ChapterForm, ChapterWriteForm, ManuscriptForm
from .models import Book, Chapter, Manuscript


@author_access_required
def book_list(request):
    user = request.user
    books = Book.objects.filter(author=user)
    if request.META.get("HTTP_HX_REQUEST"):
        return render(request, "books/fragments/list.html", {"books": books})
    return render(request, "books/list.html", {"books": books})


@author_access_required
def project_books(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    books = Book.objects.filter(project=project)
    if request.META.get("HTTP_HX_REQUEST"):
        return render(request, "books/fragments/list.html", {"books": books})
    return render(request, "books/list.html", {"books": books})


@author_access_required
def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapters = book.chapters.all()
    if request.META.get("HTTP_HX_REQUEST"):
        return render(
            request, "books/fragments/detail.html", {"book": book, "chapters": chapters}
        )
    return render(request, "books/detail.html", {"book": book, "chapters": chapters})


def book_create(request):
    form = BookForm(author=request.user)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author_id = request.user.id
            if not book.slug and book.name:
                book.slug = slugify(book.name)
            book.save()
            return redirect("books:list")
        else:
            return render(request, "books/create.html", {"form": form})
    return render(request, "books/create.html", {"form": form})


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
            return redirect("books:detail", book_slug)
    return render(request, "books/chapters/create.html", {"form": form, "book": book})


def chapter_detail(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    chapter = {**chapter.__dict__}
    chapter["word_count"] = len(chapter["text_content"].split())
    return render(
        request, "books/chapters/detail.html", {"chapter": chapter, "book": book}
    )


def chapter_edit(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    form = ChapterForm(instance=chapter)
    if request.META.get("HTTP_HX_REQUEST") and request.method == "POST":
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return render(
                request,
                "books/chapters/detail.html",
                {"book": book, "chapter": chapter},
            )
    return render(
        request,
        "books/chapters/edit.html",
        {"form": form, "book": book, "chapter": chapter},
    )


def chapter_delete(request, book_slug, chp_slug):
    book = get_object_or_404(Book, slug=book_slug)
    chapter = get_object_or_404(Chapter, id=chp_slug)
    if request.method == "POST":
        chapter.delete()
        chapters = book.chapters.all()
        return render(
            request, "books/detail.html", {"chapters": chapters, "book": book}
        )
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
        print(request.META.get("HTTP_HX_REQUEST"))
        form = ChapterWriteForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("books:chapter-detail", book_slug, chp_slug)
        else:
            return render(
                request,
                "books/chapters/detail.html",
                {"form": form, "chapter": chapter, "book": book},
            )
    elif request.method == "POST":
        form = ChapterWriteForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("books:chapter-detail", book_slug, chp_slug)
    chapter = {**chapter.__dict__}
    chapter["word_count"] = len(chapter["text_content"].split())
    return render(
        request,
        "books/chapters/write.html",
        {"form": form, "chapter": chapter, "book": book},
    )


def create_manuscript(request):
    form = ManuscriptForm()
    if request.method == "POST":
        form = ManuscriptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books:manuscripts")
    return render(
        request,
        "books/manuscripts/create.html",
        {"form": form},
    )


@author_access_required
def manuscripts(request):
    manuscripts = Manuscript.objects.filter(book__author=request.user)
    if request.META.get("HTTP_HX_REQUEST"):
        return render(
            request,
            "books/fragments/manuscripts-list.html",
            {"manuscripts": manuscripts},
        )
    return render(request, "books/manuscripts/list.html", {"manuscripts": manuscripts})


@author_access_required
def book_manuscripts(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    manuscripts = Manuscript.objects.filter(book=book)
    if request.META.get("HTTP_HX_REQUEST"):
        return render(
            request,
            "books/fragments/manuscripts-list.html",
            {"manuscripts": manuscripts},
        )
    return render(request, "books/manuscripts/list.html", {"manuscripts": manuscripts})
