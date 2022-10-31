from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .serializers import *
# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })
    
class UserList(generics.ListAPIView):#userlist
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class UserDetail(generics.RetrieveAPIView):#show every user
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListTodo(generics.ListAPIView): #Read
    queryset=Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailTodo(generics.RetrieveUpdateAPIView): #update
     queryset=Task.objects.all()
     serializer_class=TaskSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
class CreateTodo(generics.CreateAPIView): #create
    queryset=Task.objects.all()
    serializer_class=TaskSerializer   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
class DeleteTodo(generics.DestroyAPIView): #delete
    queryset=Task.objects.all()
    serializer_class=TaskSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]