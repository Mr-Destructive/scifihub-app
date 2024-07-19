from random import randint

from django.shortcuts import redirect, render
from scifihub.author.models import DailyMetric, UserMetric
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
    user = request.user
    if user:
        projects = Project.objects.filter(author=user)
        worlds = World.objects.filter(author=user)
        characters = Character.objects.filter(project__author=user)
        magic_systems = MagicSystem.objects.filter(project__author=user)
        books = Book.objects.filter(author=user)
        if not UserMetric.objects.filter(user=user).first():
            UserMetric.objects.create(user=user)
        word_count = UserMetric.objects.get(user=user).total_word_count
        if not DailyMetric.objects.filter(user=user).first():
            DailyMetric.objects.create(user=user)
        daily_metrics = DailyMetric.objects.filter(user=user).order_by('date')
        
        labels = [metric.date.strftime('%Y-%m-%d') for metric in daily_metrics]
        daily_metrics = [randint(0, 100) for _ in range(365)]
        data = [metric for metric in daily_metrics]
        
        response = {
            "username": request.user.username,
            "projects": len(projects),
            "books": len(books),
            "worlds": len(worlds),
            "characters": len(characters),
            "magic_systems": len(magic_systems),
            "word_count": word_count,
            'user': user,
            'daily_metrics': daily_metrics,
            'labels': labels,
            'data': data,
        }
        return render(request, "accounts/profile.html", context=response)
