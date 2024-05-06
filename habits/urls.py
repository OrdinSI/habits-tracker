from django.urls import path

from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView

urlpatterns = [
    path("habit/create", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habit/", HabitListAPIView.as_view(), name="habit-list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habit/delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit-delete"),
]
