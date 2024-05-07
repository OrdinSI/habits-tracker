from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config import settings


class WeekDay(models.Model):
    """Model definition for WeekDay."""

    DAY_CHOICES = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    day = models.IntegerField(
        verbose_name="день недели", choices=DAY_CHOICES, unique=True
    )

    def __str__(self):
        return self.get_day_display()

    class Meta:
        verbose_name = "день недели"
        verbose_name_plural = "дни недели"


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
    time = models.TimeField(default="12:00:00", verbose_name="время")
    is_pleasant = models.BooleanField(verbose_name="признак приятности", default=False)
    linked_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="связь", **settings.NULLABLE
    )
    days = models.ManyToManyField(WeekDay, verbose_name="дни(периодичность)")
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

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            all_days = WeekDay.objects.all()
            self.days.set(all_days)

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
