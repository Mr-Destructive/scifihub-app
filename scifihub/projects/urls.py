from django.urls import include, path

from . import views

app_name = "projects"

urlpatterns = [
    path("", views.list_projects, name="list"),
    path("create/", views.create_project, name="create"),
    path("p/<slug:project_slug>/", views.detail_project, name="detail"),
    path("p/update/<slug:project_slug>/", views.update_project, name="edit"),
    path("p/delete/<slug:project_slug>/", views.delete_project, name="delete"),
    path("p/create-book/<slug:project_slug>/", views.create_book, name="create-book"),
    path("worlds/", include("scifihub.worlds.urls")),
]
