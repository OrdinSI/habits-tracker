# Generated by Django 4.2.11 on 2024-05-03 10:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=250, verbose_name="действие")),
                ("location", models.CharField(max_length=250, verbose_name="место")),
                ("time", models.TimeField(verbose_name="время")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="признак приятности"
                    ),
                ),
                (
                    "frequency",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(7),
                        ],
                        verbose_name="периодичность(дни)",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="награда"
                    ),
                ),
                (
                    "execution_time",
                    models.IntegerField(verbose_name="время на выполнение"),
                ),
                (
                    "is_publicity",
                    models.BooleanField(
                        default=False, verbose_name="признак публикации"
                    ),
                ),
                (
                    "linked_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="связь",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]
