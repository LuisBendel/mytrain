from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Exercises(models.Model):
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=300)