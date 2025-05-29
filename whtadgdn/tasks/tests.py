from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description", completed=False)

    def test_create_task(self):
        data = {"title": "New Task", "description": "New Description", "completed": False}
        response = self.client.post("/api/tasks/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_get_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_update_task(self):
        data = {"title": "Updated Task", "description": "Updated Description", "completed": True}
        response = self.client.put(f"/api/tasks/{self.task.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)