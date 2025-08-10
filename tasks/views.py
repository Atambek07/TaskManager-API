from django.shortcuts import render
from rest_framework import generics
from . import serializers, models

class TaskListView(generics.ListAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class TaskDetailView(generics.RetrieveAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
