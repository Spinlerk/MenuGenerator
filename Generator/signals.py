from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CentralMainCourse, UserMainCourse, CentralSoup, UserSoup, CentralSalad, UserSalad, CentralSideDishes

""" This functions are made for cloning all Central tables for each user"""


@receiver(post_save, sender=User)
def clone_main_courses(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        central_courses = CentralMainCourse.objects.all()
        for central_course in central_courses:
            UserMainCourse.objects.create(
                user=instance,
                central_main_course=central_course,
                name=central_course.name,
                description=central_course.description
            )

@receiver(post_save, sender=User)
def clone_salads(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        central_salads = CentralSalad.objects.all()
        for central_salad in central_salads:
            UserSalad.objects.create(
                user=instance,
                central_salad=central_salad,
                name=central_salad.name,
                description=central_salad.description
            )

@receiver(post_save, sender=User)
def clone_soups(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        central_soups = CentralSoup.objects.all()
        for central_soup in central_soups:
            UserSoup.objects.create(
                user=instance,
                central_soup=central_soup,
                name=central_soup.name,
                description=central_soup.description
            )

@receiver(post_save, sender=User)
def clone_side_dishes(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        central_side_dishes = CentralSideDishes.objects.all()
        for central_side_dish in central_side_dishes:
            UserSalad.objects.create(
                user=instance,
                central_main_course=central_side_dish,
                name=central_side_dish.name,
                description=central_side_dish.description
            )

