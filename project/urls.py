from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("", include("scifihub.core.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("scifihub.author.urls")),
    path("projects/", include("scifihub.projects.urls")),
    path("books/", include("scifihub.book.urls")),
    path("worlds/", include("scifihub.worlds.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "scifihub.core.views.custom_404"
