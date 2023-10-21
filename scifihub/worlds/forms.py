from django import forms
from scifihub.worlds.models import World


class WorldForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of the world",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )
    description = forms.TextInput()
    world_type = forms.SelectMultiple()

    class Meta:
        model = World
        exclude = [
            "created_at",
            "updated_at",
            "completed_at",
        ]

