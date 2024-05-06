from rest_framework.exceptions import ValidationError


class LinkRewardValidator:
    """Validator for linked_habit and reward."""

    def __init__(self, linked_habit, reward):
        self.linked_habit = linked_habit
        self.reward = reward

    def __call__(self):
        if self.linked_habit and self.reward:
            raise ValidationError("Признак связи и награда не могут быть заданы одновременно.")


class LinkedHabitValidator:
    """Validator for linked_habit."""

    def __init__(self, linked_habit):
        self.linked_habit = linked_habit

    def __call__(self):
        if self.linked_habit and not self.linked_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")


class PleasantHabitValidator:
    """Validator for is_pleasant."""

    def __init__(self, is_pleasant, reward, linked_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.linked_habit = linked_habit

    def __call__(self):
        if self.is_pleasant and (self.reward or self.linked_habit):
            raise ValidationError("У приятной привычки не должно быть награды или связанной привычки.")
