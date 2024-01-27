from django.shortcuts import render
from rest_framework import viewsets
from core import serializers, models


def index(request):
    return render(request, 'core/index.html')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
