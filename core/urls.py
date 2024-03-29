from django.contrib import admin
from django.urls import path
from rest_framework import routers
from core import views


router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todos')
urlpatterns = router.urls
