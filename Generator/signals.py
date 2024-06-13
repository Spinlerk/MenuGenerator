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
)

""" This functions are made for cloning all Central tables for each user"""

def clone_items(sender, instance, created, model_class, user_model_class):
    if created and not instance.is_superuser:
        central_items = model_class.objects.all()
        for central_item in central_items:
            user_model_class.objects.create(
                user=instance,
                name=central_item.name,
                description=central_item.description,
            )

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
