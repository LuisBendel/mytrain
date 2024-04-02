# Generated by Django 5.0.3 on 2024-04-02 10:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_exercises"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SetsRepsTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutPlans",
            fields=[
                (
                    "name",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutsDay",
            fields=[
                (
                    "name",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="exercises",
            name="id",
        ),
        migrations.AddField(
            model_name="exercises",
            name="description",
            field=models.TextField(default="", max_length=1000),
        ),
        migrations.AlterField(
            model_name="exercises",
            name="name",
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="SetsRepsTimeDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("set", models.PositiveSmallIntegerField(default=0)),
                ("intensity_perc", models.PositiveIntegerField(default=100)),
                ("reps_time", models.PositiveIntegerField(default=0)),
                (
                    "sets_reps_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.setsrepstime",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutPlanUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructions", models.TextField(max_length=1000)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "workout_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.workoutplans",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("week", models.PositiveSmallIntegerField(default=0)),
                ("day", models.PositiveSmallIntegerField(default=0)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.exercises"
                    ),
                ),
                (
                    "sets_reps_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.setsrepstime",
                    ),
                ),
                (
                    "workout_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.workoutplanuser",
                    ),
                ),
                (
                    "workout_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.workoutsday",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutDayExercises",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.exercises"
                    ),
                ),
                (
                    "sets_reps_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.setsrepstime",
                    ),
                ),
                (
                    "workout_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.workoutsday",
                    ),
                ),
            ],
        ),
    ]
