from django.shortcuts import get_object_or_404, redirect, render

from scifihub.core.middlewares import author_access_required

from .forms import WorldForm
from .models import World


@author_access_required
def world_list(request):
    user = request.user
    worlds = World.objects.filter(author=user)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "world/fragments/list.html", {"worlds": worlds})
    return render(request, "worlds/list.html", {"worlds": worlds})

@author_access_required
def world_detail(request, world_slug):
    world = get_object_or_404(World, slug=world_slug)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "world/fragments/detail.html", {"world": world})
    return render(request, "worlds/detail.html", {"world": world})

@author_access_required
def world_create(request):
    if request.method == "POST":
        form = WorldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("worlds:list")
        else:
            return render(request, "worlds/create.html", {"form": form})

@author_access_required
def world_edit(request, world_slug):
    world = get_object_or_404(World, slug=world_slug)
    form = WorldForm(instance=world)
    if request.method == "POST":
        form = WorldForm(request.POST, instance=world)
        if form.is_valid():
            form.save()
            return redirect("worlds:list")
    return render(request, "worlds/edit.html", {"world": world, "form": form})

@author_access_required
def world_delete(request, world_slug):
    world = get_object_or_404(World, slug=world_slug)
    if request.method == "POST":
        world.delete()
        return redirect("worlds:list")
    return render(request, "worlds/delete.html", {"world": world})

