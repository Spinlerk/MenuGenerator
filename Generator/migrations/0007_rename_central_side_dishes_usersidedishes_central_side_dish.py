# Generated by Django 5.0.6 on 2024-05-26 14:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Generator", "0006_usermaincourse_central_main_course_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersidedishes",
            old_name="central_side_dishes",
            new_name="central_side_dish",
        ),
    ]
