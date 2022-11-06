from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import *


class TaskTests(APITestCase):

    def test_view_tasks(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('todoapp:task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """
        Ensure we can create a new task object and view object.
        """
        
        self.testuser1 = User.objects.create_superuser(username='test_user1', password='123456789')
        # self.testuser1.is_staff = True

        self.client.login(username=self.testuser1.username,password='123456789')

        data = {"title": "new", "owner": 1,"description":"desc","completed": False}
        url = reverse('todoapp:create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   