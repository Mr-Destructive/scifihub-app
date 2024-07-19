from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils import timezone


class User(AbstractUser):
    full_name = models.CharField(max_length=64)


class UserMetric(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="metrics")
    total_word_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Metrics for {self.user.username}"

    def update_total_word_count(self):
        # Calculate total word count for the user
        total_chapter_word_count = (
            Chapter.objects.filter(book__author=self.user).aggregate(
                total_word_count=Sum(models.Length("text_content"))
            )["total_word_count"]
            or 0
        )
        total_project_word_count = sum(
            len(project.description.split()) for project in self.user.projects.all()
        )
        total_character_word_count = sum(
            len(character.attributes.split())
            for character in self.user.characters.all()
        )
        total_world_word_count = sum(
            len(world.description.split()) for world in self.user.worlds.all()
        )
        total_magic_system_word_count = sum(
            len(magic_system.description.split())
            for magic_system in self.user.magic_systems.all()
        )

        self.total_word_count = (
            total_chapter_word_count
            + total_project_word_count
            + total_character_word_count
            + total_world_word_count
            + total_magic_system_word_count
        )
        self.save()

    def __str__(self):
        return f"Metrics for {self.user.username}"

    class Meta:
        verbose_name = "User Metric"
        verbose_name_plural = "User Metrics"


class DailyMetric(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="daily_metrics"
    )
    date = models.DateField(default=timezone.now)
    word_count = models.IntegerField(default=0)

    def update_word_count(self):
        # Calculate and update word count for the current day
        total_chapter_word_count = (
            Chapter.objects.filter(
                book__author=self.user, created_at__date=self.date
            ).aggregate(total_word_count=Sum(models.Length("text_content")))[
                "total_word_count"
            ]
            or 0
        )
        total_project_word_count = sum(
            len(project.description.split())
            for project in self.user.projects.filter(created_at__date=self.date)
        )
        total_character_word_count = sum(
            len(character.attributes.split())
            for character in self.user.characters.filter(created_at__date=self.date)
        )
        total_world_word_count = sum(
            len(world.description.split())
            for world in self.user.worlds.filter(created_at__date=self.date)
        )
        total_magic_system_word_count = sum(
            len(magic_system.description.split())
            for magic_system in self.user.magic_systems.filter(
                created_at__date=self.date
            )
        )

        self.word_count = (
            total_chapter_word_count
            + total_project_word_count
            + total_character_word_count
            + total_world_word_count
            + total_magic_system_word_count
        )
        self.save()

    def __str__(self):
        return f"{self.date} - {self.user.username}"

    class Meta:
        unique_together = ("user", "date")
        verbose_name = "Daily Metric"
        verbose_name_plural = "Daily Metrics"
