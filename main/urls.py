from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("exercises/", views.exercises, name="Exercises"),
    path("workout/<int:year>/<int:month>/<int:day>/", views.workout, name="Workout")
]