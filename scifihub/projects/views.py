from django.shortcuts import get_object_or_404, render

from scifihub.book.forms import BookForm
from scifihub.book.models import Book
from scifihub.core.middlewares import author_access_required

from .forms import ProjectEditForm, ProjectForm
from .models import Project


@author_access_required
def list_projects(request):
    authot = request.user
    projects = Project.objects.filter(author=authot)
    return render(request, "projects/list.html", {"projects": projects})


@author_access_required
def detail_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    author = request.user
    project_books = Book.objects.filter(author=author, project_id=project.id)
    return render(
        request, "projects/detail.html", {"project": project, "books": project_books}
    )


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return render(request, "projects/detail.html", {"project": project})
    else:
        form = ProjectForm()
        return render(request, "projects/create.html", {"form": form})


def update_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    if request.method == "POST":
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return render(request, "projects/detail.html", {"project": project})
    else:
        project = get_object_or_404(Project, slug=project_slug)
        form = ProjectEditForm(instance=project)
        return render(request, "projects/edit.html", {"form": form})


def delete_project(request, project_slug):
    if request.method == "POST":
        project = get_object_or_404(Project, slug=project_slug)
        project.delete()
        return render(request, "projects/list.html")
    else:
        project = get_object_or_404(Project, slug=project_slug)
        return render(request, "projects/delete.html", {"project": project})


@author_access_required
def create_book(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.project = project
            book.save()
            return render(request, "projects/detail.html", {"project": project})
        else:
            return render(request, "projects/create-book.html", {"form": form})
    else:
        form = BookForm()
        return render(request, "projects/create-book.html", {"form": form})
