from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.task

