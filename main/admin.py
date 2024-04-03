from django.contrib import admin
from .models import ToDoItem, Exercises, SetsRepsTime, SetsRepsTimeDetails, WorkoutDayExercises, WorkoutsDay, WorkoutPlans, WorkoutPlanUser, WorkoutSchedule

# Register your models here.
admin.site.register(ToDoItem)
admin.site.register(Exercises)
admin.site.register(SetsRepsTime)
admin.site.register(SetsRepsTimeDetails)
admin.site.register(WorkoutDayExercises)
admin.site.register(WorkoutsDay)
admin.site.register(WorkoutPlans)
admin.site.register(WorkoutPlanUser)
admin.site.register(WorkoutSchedule)