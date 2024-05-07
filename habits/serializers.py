from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from habits.models import Habit, WeekDay
from habits.validators import (
    LinkRewardValidator,
    LinkedHabitValidator,
    PleasantHabitValidator,
)


class HabitSerializer(ModelSerializer):
    """Serializer for Habit model."""

    days = PrimaryKeyRelatedField(
        many=True, queryset=WeekDay.objects.all(), required=False
    )

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
