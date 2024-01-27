from django.db import models


class Todo(models.Model):
    title = models.CharField('Название', max_length=255)
