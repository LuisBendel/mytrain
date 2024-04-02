from django.contrib import admin
from .models import ToDoItem, Exercises

# Register your models here.
admin.site.register(ToDoItem)
admin.site.register(Exercises)