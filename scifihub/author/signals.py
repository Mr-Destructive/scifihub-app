from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from scifihub.author.models import User
from scifihub.author.models import UserMetric, DailyMetric
from scifihub.book.models import Chapter
from scifihub.projects.models import Project
from scifihub.worlds.models import Character, World, MagicSystem


@receiver(post_save, sender=Chapter)
@receiver(post_save, sender=Project)
@receiver(post_save, sender=Character)
@receiver(post_save, sender=World)
@receiver(post_save, sender=MagicSystem)
def update_user_metrics(sender, instance, created, **kwargs):
    if created:
        user = instance.author

        # Update UserMetric
        user_metrics, created = UserMetric.objects.get_or_create(user=user)
        user_metrics.update_total_word_count()

        # Update DailyMetric for today
        today = timezone.now().date()
        daily_metric, created = DailyMetric.objects.get_or_create(user=user, date=today)
        daily_metric.update_word_count()
