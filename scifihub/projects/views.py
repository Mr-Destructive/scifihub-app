from datetime import datetime
from django.http import response
from django.shortcuts import get_object_or_404, render

from scifihub.book.models import Book
from scifihub.book.forms import BookForm

from .forms import ProjectForm, ProjectEditForm

from .models import Project


def list_projects(request):
    authot = request.user
    projects = Project.objects.filter(author=authot)
    return render(request, "projects/list.html", {"projects": projects})


def detail_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    author = request.user
    if project.author != author:
        return response.HttpResponseForbidden
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


def update_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return render(request, "projects/detail.html", {"project": project})
    else:
        project = get_object_or_404(Project, slug=slug)
        form = ProjectEditForm(instance=project)
        return render(request, "projects/edit.html", {"form": form})


def delete_project(request, slug):
    if request.method == "POST":
        project = get_object_or_404(Project, slug=slug)
        project.delete()
        return render(request, "projects/list.html")
    else:
        project = get_object_or_404(Project, slug=slug)
        return render(request, "projects/delete.html", {"project": project})


def create_book(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.project = project
            book.save()
            return render(request, 'projects/detail.html', {'project': project})
    else:
        form = BookForm()
        return render(request, 'projects/create-book.html', {'form': form})
