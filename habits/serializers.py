from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    LinkRewardValidator,
    LinkedHabitValidator,
    PleasantHabitValidator,
)


class HabitSerializer(ModelSerializer):
    """Serializer for Habit model."""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            LinkRewardValidator(linked_habit="linked_habit", reward="reward"),
            LinkedHabitValidator(linked_habit="linked_habit"),
            PleasantHabitValidator(
                is_pleasant="is_pleasant", reward="reward", linked_habit="linked_habit"
            ),
        ]
