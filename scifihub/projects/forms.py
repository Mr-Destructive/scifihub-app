from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]

        widgets = {
                    "visibility": forms.RadioSelect(
                        choices=Project.visiblity_types.choices
                    ),
                    "status": forms.RadioSelect(
                        choices=Project.status_types.choices
                    ),
                    "name": forms.TextInput(
                        attrs={"placeholder": "Title of the project",
                               "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
                               }
                    ),
                    "description": forms.Textarea(
                        attrs={"placeholder": "Description of the project",
                               "class": "borderless-textarea w-full bg-transparent text-black p-2 text-lg",
                               "row": "2",
                               }
                    ),
                }


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["author", "created_at", "updated_at", "completed_at", "slug"]
