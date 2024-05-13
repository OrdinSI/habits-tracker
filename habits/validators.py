from rest_framework.exceptions import ValidationError

from habits.models import Habit


class LinkRewardValidator:
    """Validator for linked_habit and reward."""

    def __init__(self, linked_habit, reward):
        self.linked_habit = linked_habit
        self.reward = reward

    def __call__(self, value):
        value_dict = dict(value)
        val_1 = value_dict.get(self.linked_habit)
        val_2 = value_dict.get(self.reward)
        if val_1 and val_2:
            raise ValidationError(
                "Признак связи и награда не могут быть заданы одновременно."
            )


class LinkedHabitValidator:
    """Validator for linked_habit."""

    def __init__(self, linked_habit):
        self.linked_habit = linked_habit

    def __call__(self, value):
        value = dict(value).get(self.linked_habit)
        if value and Habit.objects.filter(id=value.id, is_pleasant=False).exists():
            raise ValidationError("Связанная привычка должна быть приятной.")


class PleasantHabitValidator:
    """Validator for is_pleasant."""

    def __init__(self, is_pleasant, reward, linked_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.linked_habit = linked_habit

    def __call__(self, value):
        value_dict = dict(value)
        val_1 = value_dict.get(self.is_pleasant)
        val_2 = value_dict.get(self.reward)
        val_3 = value_dict.get(self.linked_habit)
        if val_1 and (val_2 or val_3):
            raise ValidationError(
                "У приятной привычки не должно быть награды или связанной привычки."
            )


class PeriodicityValidator:
    """Validator for periodicity."""

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        value = dict(value).get(self.periodicity)
        if isinstance(value, int) and (value > 7 or value < 1):
            raise ValidationError("Периодичность должна быть от 1 до 7.")


class ExecutionTimeValidator:
    """Validator for execution_time."""

    def __init__(self, execution_time):
        self.execution_time = execution_time

    def __call__(self, value):
        value = dict(value).get(self.execution_time)
        if isinstance(value, int) and (value > 120 or value < 1):
            raise ValidationError("Время выполнения должно быть от 1 до 120 секунд.")
