from django.urls import path

from . import views

app_name = "worlds"

urlpatterns = [
    path("", views.world_list, name="list"),
    path(
        "project-worlds/<slug:project_slug>/",
        views.project_worlds,
        name="project-worlds",
    ),
    path("create/", views.world_create, name="create"),
    path("<int:world_id>/", views.world_detail, name="detail"),
    path("edit/<int:world_id>/", views.world_edit, name="edit"),
    path("delete/<int:world_id>/", views.world_delete, name="delete"),
    path("characters/list/<slug:project_slug>/", views.characters, name="characters"),
    path(
        "characters/<slug:project_slug>/create/",
        views.character_create,
        name="character-create",
    ),
    path(
        "characters/<slug:character_slug>/",
        views.character_detail,
        name="character-detail",
    ),
    path(
        "characters/<slug:character_slug>/edit/",
        views.character_edit,
        name="character-edit",
    ),
    path(
        "characters/<slug:character_slug>/delete/",
        views.character_delete,
        name="character-delete",
    ),
    path("magicsys/list/", views.magic_systems, name="magic-systems"),
    path(
        "magicsys/list/<slug:project_slug>/",
        views.project_magic_systems,
        name="project-magic-systems",
    ),
    path("magicsys/create/", views.magic_system_create, name="magic-system-create"),
    path(
        "magicsys/<slug:project_slug>/<int:magic_sys_id>/",
        views.magic_system_detail,
        name="magic-system-detail",
    ),
]
