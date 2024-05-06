from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from habits.models import Habit
from habits.pagination import HabitPagination
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """Class for creating a new habit."""
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    """Class for listing all habits."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination


class HabitRetrieveAPIView(RetrieveAPIView):
    """Class for getting a habit."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """Class for updating a habit."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteAPIView(RetrieveAPIView):
    """Class for deleting a habit."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
