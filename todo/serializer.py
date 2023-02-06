from rest_framework import serializers
from todo.models import User, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # Todos os campos '__all__'
        fields = ['name', 'email', 'url']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
