from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Class for testing user views."""

    def setUp(self):
        self.user = User.objects.create(email="test1@localhost")
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        """Test list of users."""
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_detail(self):
        """Test detail of user."""
        response = self.client.get(f"/users/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("email"), "test1@localhost")

    def test_user_update(self):
        """Test update of user."""
        data = {
            "email": "test2@localhost",
        }
        response = self.client.patch(f"/users/{self.user.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "test2@localhost")

    def test_user_delete(self):
        """Test delete of user."""
        response = self.client.delete(f"/users/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_create(self):
        """Test create of user."""
        data = {
            "email": "test3@localhost",
            "password": "test",
        }
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("email"), "test3@localhost")
