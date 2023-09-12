from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = [
            "author",
            "created_at",
            "updated_at",
            "completed_at",
        ]
