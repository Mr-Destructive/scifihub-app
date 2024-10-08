from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from scifihub.book.forms import ChapterWriteForm


@login_required
def index(request):
    return render(request, "index.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


def editor(request):
    form = ChapterWriteForm()
    return render(request, "editor.html", {"form": form})
