"""Models of database tables"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class Profile(models.Model):
    """
    User profile model
    A testing model that extends the User model with a one-to-one relationship.
    The Profile model is linked directly to the Django User model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class BaseCourse(models.Model):
    """An abstract base class for course-related models, containing common fields like name,
    description, created_at, and updated_at."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""

        abstract = True


class CentralMainCourse(BaseCourse):
    """Models for the central database, intended for admin management.
    These models inherit from BaseCourse and include additional indexing and ordering.
    """

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


"""User-specific models that clone central models when a new user is created.
After cloning just user can manage his database whit tools like adding, deleting and editing courses.
These models include a foreign key relationship to the User model 
and additional fields such as last_used."""


class UserMainCourse(BaseCourse):
    """User main course model"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Main_courses"
    )
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSoup(BaseCourse):
    """Central soup model"""

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSoup(BaseCourse):
    """User soup model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Soup")
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSalad(BaseCourse):
    """Central salad model"""

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSalad(BaseCourse):
    """User salad model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Salad")
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class CentralSideDishes(BaseCourse):
    """Central side dishes model"""

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.description}"


class UserSideDishes(BaseCourse):
    """User side dishes model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SideDishes")

    class Meta:
        """Metaclass for ordering by name."""

        ordering = (Lower("name"),)
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} - {self.description}"


class DailyMenu(models.Model):
    """Model for creatíng daily menu function - A model to represent a user's daily menu,
    linking to user-specific courses (soups, main courses, salads, and side dishes)
    and including the date of the menu.The DailyMenu model creates a daily menu for users,
    allowing multiple main courses and side dishes."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    soup = models.ForeignKey(UserSoup, on_delete=models.SET_NULL, blank=True, null=True)
    main_course = models.ManyToManyField(UserMainCourse)
    side_dishes = models.ManyToManyField(UserSideDishes, blank=True)
    salad = models.ForeignKey(
        UserSalad, on_delete=models.SET_NULL, blank=True, null=True
    )
