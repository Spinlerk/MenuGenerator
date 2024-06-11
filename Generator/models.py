from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower

""" Central tables are made for admin, so he can easily edit them. """


class CentralMainCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


""" User tables will be cloned from Central tables when new user is created. """


class UserMainCourse(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Main_courses"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSoup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSoup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Soup")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSalad(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSalad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Salad")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSideDishes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (Lower('name'),)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSideDishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SideDishes")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    ordering = (Lower('name'),)
    indexes = [
        models.Index(fields=['name'])
    ]

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
