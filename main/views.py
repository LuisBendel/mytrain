from django.shortcuts import render
from .models import ToDoItem, Exercises

# Create your views here.
def home(request):
    return render(request, "home.html")

def exercises(request):
    items = Exercises.objects.all()
    return render(request, "exercises.html", {"Exercises": items})
