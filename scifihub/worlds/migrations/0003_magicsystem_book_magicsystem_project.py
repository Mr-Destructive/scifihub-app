# Generated by Django 4.2.3 on 2023-11-01 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
        ("book", "0001_initial"),
        ("worlds", "0002_alter_character_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="magicsystem",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="book.book",
            ),
        ),
        migrations.AddField(
            model_name="magicsystem",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.project",
            ),
        ),
    ]
