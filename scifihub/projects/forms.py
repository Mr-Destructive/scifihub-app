from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title of the project",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )
    description = forms.CharField(
        label=False,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description of the project",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
                "rows": 3,
            }
        ),
    )
    visibility = forms.ChoiceField(
        label="Visibility",
        choices=Project.visibility_types.choices,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    status = forms.ChoiceField(
        label="Status",
        choices=Project.status_types.choices,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    project_type = forms.CharField(
        max_length=128,
        label="Project Type",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type of the project",
            }
        ),
    )

    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]
