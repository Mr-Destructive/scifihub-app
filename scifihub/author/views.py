from django.shortcuts import redirect, render
from scifihub.author.models import UserMetric
from scifihub.book.models import Book
from scifihub.worlds.models import World, MagicSystem, Character

from scifihub.projects.models import Project

from .forms import AuthorCreationForm


def register(request):
    if request.method == "POST":
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "accounts/register.html", {"form": form})
    else:
        form = AuthorCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def profile(request):
    projects = Project.objects.filter(author=request.user)
    worlds = World.objects.filter(author=request.user)
    characters = Character.objects.filter(project__author=request.user)
    magic_systems = MagicSystem.objects.filter(project__author=request.user)
    books = Book.objects.filter(author=request.user)
    if not UserMetric.objects.filter(user=request.user).first():
        UserMetric.objects.create(user=request.user)
    word_count = UserMetric.objects.get(user=request.user).total_word_count

    response = {
        "username": request.user.username,
        "projects": len(projects),
        "books": len(books),
        "worlds": len(worlds),
        "characters": len(characters),
        "magic_systems": len(magic_systems),
        "word_count": word_count,
    }
    return render(request, "accounts/profile.html", context=response)
