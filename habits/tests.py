from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Class for testing habit views."""

    def setUp(self):
        self.user = User.objects.create(email="test1@localhost")
        self.habit = Habit.objects.create(
            action="test", location="test", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        """Test list of habits."""
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_habit_detail(self):
        """Test detail of habit."""
        response = self.client.get(f"/habits/{self.habit.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("action"), "test")

    def test_habit_update(self):
        """Test update of habit."""
        data = {
            "action": "test2",
        }
        response = self.client.patch(f"/habits/update/{self.habit.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "test2")

    def test_habit_delete(self):
        """Test delete of habit."""
        response = self.client.delete(f"/habits/delete/{self.habit.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_create(self):
        """Test create of habit."""
        data = {
            "action": "test3",
            "location": "test3",
            "owner": self.user.id,
        }
        response = self.client.post("/habits/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("action"), "test3")
