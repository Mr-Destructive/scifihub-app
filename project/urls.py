from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("scifihub.core.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("scifihub.author.urls")),
    path("projects/", include("scifihub.projects.urls")),
    path("books/", include("scifihub.book.urls")),
]
