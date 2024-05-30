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
    last_used = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}({self.description}), last used: {self.last_used}"


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
    last_used = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}({self.description}), last used: {self.last_used}"


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
    last_used = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}({self.description}), last used: {self.last_used}"


class CentralSideDishes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class UserSideDishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='SideDishes')
    #central_side_dish = models.ForeignKey(CentralSideDishes, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}({self.description}), last used: {self.last_used}"


class WeeklyMenu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DailyMenu(models.Model):
    weekly_menu = models.ForeignKey(WeeklyMenu, on_delete=models.CASCADE, related_name='daily_menus')
    day = models.CharField(max_length=9, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')])
    soup = models.ForeignKey(UserSoup, on_delete=models.SET_NULL, null=True, blank=True, related_name='soup')
    main_course = models.ForeignKey(UserMainCourse, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_course')
    side_dish = models.ForeignKey(UserSideDishes, on_delete=models.SET_NULL, null=True, blank=True)
    salad = models.ForeignKey(UserSalad, on_delete=models.SET_NULL, null=True, blank=True, related_name='salad')