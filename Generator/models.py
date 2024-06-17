from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower

"""Models are models of database tables"""


"""# A testing model that extends the User model with a one-to-one relationship. 
The Profile model is linked directly to the Django User model."""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


"""An abstract base class for course-related models, containing common fields like name, 
description, created_at, and updated_at."""

class BaseCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


""" Models for the central database, intended for admin management. 
These models inherit from BaseCourse and include additional indexing and ordering. """


class CentralMainCourse(BaseCourse):

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


""" User-specific models that clone central models when a new user is created. 
After cloning just user can manage his database whit tools like adding, deleting and editing courses.
These models include a foreign key relationship to the User model and additional fields such as last_used. """


class UserMainCourse(BaseCourse):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Main_courses"
    )
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSoup(BaseCourse):

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSoup(BaseCourse):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Soup")
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower("name"),)
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSalad(BaseCourse):

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSalad(BaseCourse):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Salad")
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSideDishes(BaseCourse):

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSideDishes(BaseCourse):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SideDishes")


class Meta:
    ordering = (Lower("name"),)
    indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} - {self.description}"


"""Model for creatíng daily menu function - A model to represent a user's daily menu, 
linking to user-specific courses (soups, main courses, salads, and side dishes) and including the date of the menu.
The DailyMenu model creates a daily menu for users, allowing multiple main courses and side dishes."""

class DailyMenu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    soup = models.ForeignKey(UserSoup, on_delete=models.SET_NULL, blank=True, null=True)
    main_course = models.ManyToManyField(UserMainCourse)
    side_dishes = models.ManyToManyField(UserSideDishes, blank=True)
    salad = models.ForeignKey(
        UserSalad, on_delete=models.SET_NULL, blank=True, null=True
    )
