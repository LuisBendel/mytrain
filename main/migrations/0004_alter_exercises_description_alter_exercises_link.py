# Generated by Django 5.0.3 on 2024-04-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_setsrepstime_workoutplans_workoutsday_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercises",
            name="description",
            field=models.TextField(default="", max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="exercises",
            name="link",
            field=models.CharField(max_length=300, null=True),
        ),
    ]