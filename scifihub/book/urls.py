from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="list"),
    path(
        "project-books/<slug:project_slug>/", views.project_books, name="project-books"
    ),
    path("create/", views.book_create, name="create"),
    path("book/<slug:book_slug>/", views.book_detail, name="detail"),
    path("edit/<slug:book_slug>/", views.book_edit, name="edit"),
    path("delete/<slug:book_slug>/", views.book_delete, name="delete"),
    path("manuscripts/", views.manuscripts, name="manuscripts"),
    path("manuscripts/create/", views.create_manuscript, name="manuscript-create"),
    path(
        "manuscripts/<slug:book_slug>/", views.book_manuscripts, name="book-manuscripts"
    ),
    path(
        "book/<slug:book_slug>/create/chapter/", views.add_chapter, name="create-chapter"
    ),
    path(
        "b/<slug:book_slug>/chapter/<slug:chp_slug>/",
        views.chapter_detail,
        name="chapter-detail",
    ),
    path(
        "b/<slug:book_slug>/chapter/<slug:chp_slug>/edit",
        views.chapter_edit,
        name="chapter-edit",
    ),
    path(
        "b/<slug:book_slug>/chapter/<slug:chp_slug>/delete/",
        views.chapter_delete,
        name="chapter-delete",
    ),
    path(
        "b/<slug:book_slug>/chapter/<slug:chp_slug>/write/",
        views.chapeter_write,
        name="chapter-write",
    ),
]
