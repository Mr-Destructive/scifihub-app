from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("", views.list_projects, name="list"),
    path("create/", views.create_project, name="create"),
    path("p/<slug:slug>/", views.detail_project, name="detail"),
    path("p/update/<slug:slug>/", views.update_project, name="edit"),
    path("p/delete/<slug:slug>/", views.delete_project, name="delete"),
    path('p/create-book/<slug:slug>/', views.create_book, name='create-book'),
]
