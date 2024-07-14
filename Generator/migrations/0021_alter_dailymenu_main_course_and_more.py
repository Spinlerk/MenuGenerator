# Generated by Django 4.0 on 2024-07-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0020_alter_usersidedishes_options_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymenu',
            name='main_course',
            field=models.ManyToManyField(to='Generator.UserMainCourse'),
        ),
        migrations.AlterField(
            model_name='dailymenu',
            name='side_dishes',
            field=models.ManyToManyField(blank=True, to='Generator.UserSideDishes'),
        ),
    ]