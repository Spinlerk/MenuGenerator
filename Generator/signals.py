"""Signals clones the central databases when new user is created,
central database has predefined courses but each user can manage the database by
their own specific way they can add, edit, delete."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import (
    CentralMainCourse,
    UserMainCourse,
    CentralSoup,
    UserSoup,
    CentralSalad,
    UserSalad,
    CentralSideDishes,
    UserSideDishes,
    Profile,
)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """This signal receiver creates a Profile instance for each new User instance. It ensures that every user has an associated profile."""
    if created:
        Profile.objects.create(user=instance)





def clone_items(sender, instance, created, model_class, user_model_class):
    """This function clones all items from a central model to the corresponding user-specific model
    when a new user is created. It checks if the user is not a superuser and then iterates over all central items,
    creating corresponding user-specific items."""
    if created and not instance.is_superuser:
        central_items = model_class.objects.all()
        for central_item in central_items:
            user_model_class.objects.create(
                user=instance,
                name=central_item.name,
                description=central_item.description,
            )


"""Signal receivers to clone items from central tables to user-specific tables when a new user is created."""


@receiver(post_save, sender=User)
def clone_main_courses(sender, instance, created, **kwargs):
    clone_items(sender, instance, created, CentralMainCourse, UserMainCourse)


@receiver(post_save, sender=User)
def clone_salads(sender, instance, created, **kwargs):
    clone_items(sender, instance, created, CentralSalad, UserSalad)


@receiver(post_save, sender=User)
def clone_soups(sender, instance, created, **kwargs):
    clone_items(sender, instance, created, CentralSoup, UserSoup)


@receiver(post_save, sender=User)
def clone_side_dishes(sender, instance, created, **kwargs):
    clone_items(sender, instance, created, CentralSideDishes, UserSideDishes)
