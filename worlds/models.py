from django.db import models
from django.template.defaultfilters import default
from author.models import User

from book.models import Book
from projects.models import Project


class World(models.Model):
    class world_types(models.TextChoices):
        universe = "universe", "Universe"
        planet = "planet", "Planet"
        continent = "continent", "Continent"
        empire = "empire", "Empire"
        country = "country", "Country"
        kingdom = "kingdom", "Kingdom"
        state = "state", "State"
        region = "region", "Region"
        city = "city", "City"
        town = "town", "Town"

    name = models.CharField(max_length=128, unique=True)
    world_type = models.CharField(
        max_length=32, choices=world_types.choices, default=world_types.kingdom
    )
    description = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.world_type + " : " + self.name


class Character(models.Model):
    class character_types(models.TextChoices):
        protagonist = "protagonist", "Protagonist"
        antagonist = "antagonist", "Antagonist"
        side_kick = "side_kick", "Side Kick"
        love_interest = "love_interest", "Love Interest"
        mentor = "mentor", "Mentor"
        ally = "ally", "Ally"
        spirit = "spirit", "Spirit"
        human = "human", "Human"
        non_human = "non_human", "Non-Human"
        animal = "animal", "Animal"
        monster = "monster", "Monster"

    name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    character_type = models.CharField(
        max_length=32,
        choices=character_types.choices,
        default=character_types.human,
    )
    bio = models.TextField()
    attributes = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=128)
    desription = models.TextField()
    attributes = models.TextField()
    world = models.ForeignKey(World, on_delete=models.SET_NULL, null=True, blank=True)


class Location(models.Model):
    class landscape_types(models.TextChoices):
        forest = "forest", "Forest"
        island = "island", "Island"
        sea = "sea", "Sea"
        river = "river", "River"
        ocean = "ocean", "Ocean"
        mountain = "mountain", "Mountain"
        desert = "desert", "Desert"
        plains = "plains", "Plains"

    name = models.CharField(max_length=128)
    desription = models.TextField()
    attributes = models.TextField()

    world = models.ForeignKey(World, on_delete=models.SET_NULL, null=True, blank=True)

    landscape_type = models.CharField(
        max_length=32, choices=landscape_types.choices, default=landscape_types.plains
    )


class MagicSystem(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    world = models.ForeignKey(World, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name + "in" + self.world.name
