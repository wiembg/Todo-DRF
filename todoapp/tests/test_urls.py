from django.test import SimpleTestCase
from django.urls import reverse,resolve
from todoapp.views import *
#cmd:python manage.py test

class TestUrls(SimpleTestCase):
    def test_equal(self):
        self.assertEqual(1,3)   
    def test_tasks_list_url_is_resolved(self):
        url=reverse('task-list')
        f=resolve(url).func.__name__
        f1=ListTodo.as_view().__name__
        self.assertEquals(f,f1)
    def test_users_list_url_is_resolved(self):
        url=reverse('user-list')
        f=resolve(url).func.__name__
        f1=UserList.as_view().__name__
        self.assertEquals(f,f1)       



