from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]
