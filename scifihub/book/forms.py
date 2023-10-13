from django import forms
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

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Title of the book",
                    "class": "borderless-text-input",
                }
            ),
            "genre": forms.TextInput(
                attrs={
                    "placeholder": "Genre of the book",
                    "class": "borderless-text-input",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "placeholder": "Slug of the book",
                    "class": "borderless-text-input",
                }
            )
        }

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

        widgets = {
            "text_content": forms.Textarea(
                attrs={
                    "placeholder": "Content of the chapter",
                    "class": "borderless-textinput",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Title of the chapter",
                    "class": "borderless-text-input",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["project"].queryset = Chapter.objects.filter(author=user)


class ChapterEditForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ["text_content",]

        widgets = {
            "text_content": forms.Textarea(
                attrs={
                    "class": "borderless-textinput",
                }
            )
        }
