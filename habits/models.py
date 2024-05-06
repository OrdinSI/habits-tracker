from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config import settings
from habits.services import get_current_time


class Habit(models.Model):
    """Model definition for Habit."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        **settings.NULLABLE
    )
    action = models.CharField(max_length=250, verbose_name="действие")
    location = models.CharField(max_length=250, verbose_name="место")
    time = models.TimeField(default=get_current_time, verbose_name="время")
    is_pleasant = models.BooleanField(verbose_name="признак приятности", default=False)
    linked_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="связь", **settings.NULLABLE
    )
    frequency = models.IntegerField(
        default=1,
        verbose_name="периодичность(дни)",
        validators=[MinValueValidator(1), MaxValueValidator(7)],
    )
    reward = models.CharField(
        max_length=250, verbose_name="награда", **settings.NULLABLE
    )
    execution_time = models.IntegerField(
        default=10,
        verbose_name="время на выполнение(сек)",
        validators=[MinValueValidator(1), MaxValueValidator(120)],
    )
    is_public = models.BooleanField(verbose_name="признак публичности", default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
