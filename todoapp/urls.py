from django.urls import path
from .views import *
from .views import SignUpView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('',api_root),   
    path("signup/", SignUpView.as_view(), name="signup"),
    path('todos/',ListTodo.as_view(),name='task-list'),
    path('create/',CreateTodo.as_view(),name='create'),
    path('todos/<int:pk>/',DetailTodo.as_view(),name='task-detail'),
    path('delete/<int:pk>',DeleteTodo.as_view(), name="task-delete"),
    path('users/',UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail')
])