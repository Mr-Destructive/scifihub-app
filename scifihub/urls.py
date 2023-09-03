from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('book.urls')),
    path("projects/", include('projects.urls')),
]
