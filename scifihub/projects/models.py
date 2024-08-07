from django.db import models
from django.shortcuts import get_object_or_404

from scifihub.author.models import User
from scifihub.core.models import TimeStampedModel
from scifihub.core.utils import get_or_set_slug


class Project(TimeStampedModel):
    class visibility_types(models.TextChoices):
        public = "public", "Public"
        private = "private", "Private"

    class status_types(models.TextChoices):
        published = "published", "Published"
        draft = "draft", "Draft"

    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    visibility = models.CharField(
        max_length=128,
        choices=visibility_types.choices,
        default=visibility_types.private,
    )
    status = models.CharField(
        max_length=128,
        choices=status_types.choices,
        default=status_types.draft,
        null=True,
    )
    project_type = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        project = None
        if self.id:
            project = get_object_or_404(Project, id=self.id)
        self.slug = get_or_set_slug(self, project)
        try:
            return super().save(*args, **kwargs)
        except Exception as e:
            print(e)
