from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# All Exercises including different types of exercises
class Exercises(models.Model):
    name = models.CharField(primary_key=True, max_length=300)
    link = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, default="")
    type = {
        "LW": "Lift Weights",
        "LT": "Lift Time",
        "C": "Cardio"
    }


# Define different sets, reps and time schedules and details for each of these
class SetsRepsTime(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

class SetsRepsTimeDetails(models.Model):
    sets_reps_time = models.ForeignKey(SetsRepsTime, on_delete=models.CASCADE)
    set = models.PositiveSmallIntegerField(default=0)
    intensity_perc = models.PositiveIntegerField(default=100)
    reps_time = models.PositiveIntegerField(default=0)


# define workout plans, workout plans are assigned to one or more users
class WorkoutPlans(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    description = models.TextField(max_length=1000)

class WorkoutPlanUser(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlans, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructions = models.TextField(max_length=1000)


# A workout Day contains one or more exercises
# The workout days are organized in a workout schedule, which also includes sets and reps etc.
class WorkoutsDay(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    description = models.TextField(max_length=1000)

class WorkoutDayExercises(models.Model):
    workout_day = models.ForeignKey(WorkoutsDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    sets_reps_time = models.ForeignKey(SetsRepsTime, on_delete=models.CASCADE)

class WorkoutSchedule(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlanUser, on_delete=models.CASCADE)
    workout_day = models.ForeignKey(WorkoutsDay, on_delete=models.CASCADE)
    week = models.PositiveSmallIntegerField(default=0)
    day = models.PositiveSmallIntegerField(default=0)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    sets_reps_time = models.ForeignKey(SetsRepsTime, on_delete=models.CASCADE)