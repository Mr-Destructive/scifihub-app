from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from scifihub.book.models import Book, Chapter


def author_access_required(view_func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        book_slug = kwargs.get("slug")
        if book_slug:
            book = get_object_or_404(Book, slug=book_slug)
            if book.author != request.user:
                raise PermissionDenied

        chapter_id = kwargs.get("chapter_id")
        if chapter_id:
            chapter = get_object_or_404(Chapter, id=chapter_id)
            if chapter.book.author != request.user:
                raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrap
