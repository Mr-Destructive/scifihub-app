from django.forms import ModelForm

from .models import Book, Chapter


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = [
            "author",
            "created_at",
            "updated_at",
            "completed_at",
        ]


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        exclude = [
            "book",
            "created_at",
            "updated_at",
            "completed_at",
            "section",
        ]
