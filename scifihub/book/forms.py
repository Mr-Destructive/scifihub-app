from django import forms
from django.forms import ModelForm

from .models import Book, Chapter


class BookForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title of the book",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )
    genre = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Genre of the book",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        )
    )
    slug = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slug of the book",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )
    
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
    text_content = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Content of the chapter",
                "class": "borderless-textinput",
            }
        )
    )
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title of the chapter",
                "class": "borderless-text-input ",
            }
        ),
    )

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


class ChapterWriteForm(ModelForm):
    text_content = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Content of the chapter",
                "class": "borderless-textinput",
            }
        )
    )
    class Meta:
        model = Chapter
        fields = ["text_content",]

