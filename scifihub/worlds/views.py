from django.shortcuts import get_object_or_404, redirect, render

from scifihub.core.middlewares import author_access_required
from scifihub.projects.models import Project

from .forms import CharacterForm, MagicSystemForm, WorldForm
from .models import Character, MagicSystem, World


@author_access_required
def world_list(request):
    user = request.user
    worlds = World.objects.filter(author=user)
    projects = []
    for world in worlds:
        project = world.project
        projects.append(project)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "world/fragments/list.html", {"worlds": worlds, "projects": projects})
    return render(request, "worlds/list.html", {"worlds": worlds, "projects": projects})

@author_access_required
def project_worlds(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    worlds = World.objects.filter(project=project)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "world/fragments/list.html", {"worlds": worlds, "project": project}) 
    return render(request, "worlds/list.html", {"worlds": worlds})

@author_access_required
def world_detail(request, world_id):
    world = get_object_or_404(World, id=world_id)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "world/fragments/detail.html", {"world": world})
    return render(request, "worlds/detail.html", {"world": world, "project": world.project})

@author_access_required
def world_create(request):
    if request.method == "POST":
        form = WorldForm(request.POST)
        if form.is_valid():
            world = form.save(commit=False)
            world.author = request.user
            world.save()
            return redirect("worlds:list")
        else:
            return render(request, "worlds/create.html", {"form": form})
    else:
        form = WorldForm()
        return render(request, "worlds/create.html", {"form": form})

@author_access_required
def world_edit(request, world_id):
    world = get_object_or_404(World, id=world_id)
    form = WorldForm(instance=world)
    if request.method == "POST":
        form = WorldForm(request.POST, instance=world)
        if form.is_valid():
            form.save()
            return redirect("worlds:list")
    return render(request, "worlds/edit.html", {"world": world, "form": form})

@author_access_required
def world_delete(request, world_id):
    world = get_object_or_404(World, id=world_id)
    if request.method == "POST":
        world.delete()
        return redirect("worlds:list")
    return render(request, "worlds/delete.html", {"world": world})


@author_access_required
def characters(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    characters = Character.objects.filter(project__author=request.user, project__slug=project_slug)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "worlds/characters/fragments/list.html", {"character": characters, "project": project})
    return render(request, "worlds/characters/list.html", {"project": project, "characters": characters})

@author_access_required
def character_detail(request, world_id, character_id):
    world = get_object_or_404(World, id=world_id)
    character = get_object_or_404(world.characters.all(), id=character_id)
    return render(request, "worlds/characters/detail.html", {"world": world, "character": character})

@author_access_required
def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect("worlds:characters", project_slug)
        else:
            return render(request, "worlds/characters/create.html", {"form": form})
    else:
        form = CharacterForm()
        return render(request, "worlds/characters/create.html", {"form": form})


def character_edit(request, world_id, character_id):
    pass

def character_delete(request, world_id, character_id):
    pass

@author_access_required
def magic_systems(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    magic_systems = MagicSystem.objects.filter(project__author=request.user, project__slug=project_slug)
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "worlds/magic-systems/fragments/list.html", {"project": project, "magic_systems": magic_systems})
    return render(request, "worlds/magic-systems/list.html", {"project": project, "magic_systems": magic_systems})

@author_access_required
def magic_system_detail(request, world_id, magic_system_id):
    world = get_object_or_404(World, id=world_id)
    magic_system = get_object_or_404(world.magic_systems.all(), id=magic_system_id)
    return render(request, "worlds/magic-system_detail.html", {"world": world, "magic_system": magic_system})

@author_access_required
def magic_system_create(request):
    if request.method == "POST":
        form = MagicSystemForm(request.POST)
        if form.is_valid():
            magic_system = form.save(commit=False)
            magic_system.save()
            return redirect("home")
        else:
            return render(request, "worlds/magic-systems/create.html", {"form": form})
    else:
        form = MagicSystemForm()
        return render(request, "worlds/magic-systems/create.html", {"form": form})
