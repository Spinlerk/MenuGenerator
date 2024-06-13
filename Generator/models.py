from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class BaseCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


""" Central tables are made for admin, so he can easily edit them. """


class CentralMainCourse(BaseCourse):

    class Meta:
        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


""" User tables will be cloned from Central tables when new user is created. """


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


class DailyMenu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    soup = models.ForeignKey(UserSoup, on_delete=models.SET_NULL, blank=True, null=True)
    main_course = models.ManyToManyField(UserMainCourse)
    side_dishes = models.ManyToManyField(UserSideDishes, blank=True)
    salad = models.ForeignKey(
        UserSalad, on_delete=models.SET_NULL, blank=True, null=True
    )
