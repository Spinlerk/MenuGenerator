# Generated by Django 5.0.6 on 2024-05-30 14:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Generator", "0013_rename_last_used_at_usermaincourse_last_used"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weeklymenu",
            name="user",
        ),
        migrations.RemoveField(
            model_name="usersidedishes",
            name="last_used",
        ),
        migrations.DeleteModel(
            name="DailyMenu",
        ),
        migrations.DeleteModel(
            name="WeeklyMenu",
        ),
    ]
