from django.db import models
from slugify import slugify
from author.models import User
from core.models import TimeStampedModel, UUIDModel
from core.utils import get_or_set_slug

from projects.models import Project


class Book(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books_written",
    )
    genre = models.CharField(max_length=128)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        self.slug = slugify(self.name)
        book = None
        if self.id:
            book = Book.objects.get(id=self.id)
        self.slug = get_or_set_slug(self, book)
        return self.name + " : by " + self.author.username

class Section(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="sections")
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = [
            "book__id",
            "order",
        ]
        unique_together = (("book", "order"),)

    def __str__(self):
        return f"{self.book.name} -> {self.order} : {self.name}"


class Chapter(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, null=True, blank=True
    )
    book= models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name="chapters",
    )
    text_content = models.TextField()
    status = models.BooleanField(default=False, verbose_name="Publish")
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = [
            "section__order",
            "order",
        ]
        unique_together = (("section", "order"),)

    def __str__(self):
        book_name = self.book.name
        chapter_order = self.order
        return f"{book_name} : {chapter_order}"


class Revision(UUIDModel, TimeStampedModel):
    chapter = models.ForeignKey(
         Chapter, on_delete=models.CASCADE, blank=True,
         related_name="revisions"
     )
    number = models.PositiveIntegerField()

    class Meta:
        ordering = [
            "-number",
        ]


class Draft(UUIDModel, TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="drafts")
    number = models.PositiveIntegerField()
    completed_at = models.DateTimeField()

    class Meta:
        ordering = [
            "-number",
        ]


class Notes(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField()
    book_note = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, related_name="notes")

