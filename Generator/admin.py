from django.contrib import admin
from .models import (
    CentralMainCourse,
    CentralSoup,
    CentralSalad,
    CentralSideDishes,
)
from .models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]

""" These classes tel how databases below will be displayed in Django admin"""


class CentralMainCourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description", "created_at", "updated_at")


admin.site.register(CentralMainCourse, CentralMainCourseAdmin)


class CentralSoupAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description", "created_at", "updated_at")


admin.site.register(CentralSoup, CentralSoupAdmin)


class CentralSaladAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description", "created_at", "updated_at")


admin.site.register(CentralSalad, CentralSaladAdmin)


class CentralSideDishesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description", "created_at", "updated_at")


admin.site.register(CentralSideDishes, CentralSideDishesAdmin)
