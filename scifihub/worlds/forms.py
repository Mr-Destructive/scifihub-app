from django import forms
from scifihub.worlds.models import Character, MagicSystem, World


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
    description = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description of the world",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        )

    )
    world_type = forms.SelectMultiple()

    class Meta:
        model = World
        exclude = [
            "author",
            "created_at",
            "updated_at",
            "completed_at",
        ]

class CharacterForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of the character",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )
    nickname = forms.CharField(
        max_length=128,
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nickname of the character",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        )
    )
    character_type = forms.ChoiceField(
        choices=Character.character_types.choices
    )

    class Meta:
        model = Character
        exclude = [
            "created_at",
            "updated_at",
            "completed_at",
        ]

class MagicSystemForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of the magic system",
                "class": "borderless-text-input w-full bg-transparent text-white p-2 text-lg font-medium",
            }
        ),
    )

    class Meta:
        model = MagicSystem
        exclude = [
            "created_at",
            "updated_at",
            "completed_at",
        ]
