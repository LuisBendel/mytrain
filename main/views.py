from django.shortcuts import render
from .models import ToDoItem, Exercises
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required(login_url="login")
def exercises(request):
    items = Exercises.objects.all()
    return render(request, "exercises.html", {"Exercises": items})
