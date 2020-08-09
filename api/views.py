from django.shortcuts import render

from .models import Todo
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import TodoSerializer
from rest_framework import filters


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=title']
