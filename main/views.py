from django.shortcuts import render
from .models import ToDoItem, Exercises
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar, Calendar

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required(login_url="login")
def exercises(request):
    items = Exercises.objects.all()
    return render(request, "exercises.html", {"Exercises": items})

# render workout view
@login_required(login_url="login")
def workout(request, year, month, day):

    cal = calendar.Calendar()

    monthdays = cal.itermonthdays4(year=2024, month=4)

    return render(request, "workout.html",
                  {
                      "year": year,
                      "month": month,
                      "day": day,
                      "monthdays": monthdays
                  }
                  )
