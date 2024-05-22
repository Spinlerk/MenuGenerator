from django.db import models
from django.contrib.auth.models import User

""" Central tables are made for admin, so he can easily edit them. """


class CentralMainCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


""" User tables will be cloned from Central tables when new user is created. """


class UserMainCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Main_courses')
    #central_main_course = models.ForeignKey(CentralMainCourse, on_delete=models.SET_NULL, null=True, blank=True)  # tady
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CentralSoup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserSoup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Soup')
    #central_soup = models.ForeignKey(CentralSoup, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CentralSalad(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserSalad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Salad')
    #central_salad = models.ForeignKey(CentralSalad, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CentralSideDishes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserSideDishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='SideDishes')
    #central_side_dishes = models.ForeignKey(CentralSideDishes, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


