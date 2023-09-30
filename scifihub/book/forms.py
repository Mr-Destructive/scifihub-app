from django.forms import ModelForm

from scifihub.projects.models import Project

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["project"].queryset = Project.objects.filter(author=user)


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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["project"].queryset = Chapter.objects.filter(author=user)


class ChapterEditForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ["text_content",]
