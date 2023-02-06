from django.shortcuts import render
from rest_framework import viewsets
from todo.models import User, Task
from todo.serializer import UserSerializer, TaskSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
