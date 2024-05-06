from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner, IsAdmin


class HabitCreateAPIView(CreateAPIView):
    """Class for creating a new habit."""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(ListAPIView):
    """Class for listing all habits."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class HabitsPublicListAPIView(ListAPIView):
    """Class for listing all public habits."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Class for getting a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class HabitUpdateAPIView(UpdateAPIView):
    """Class for updating a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class HabitDeleteAPIView(RetrieveAPIView):
    """Class for deleting a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
