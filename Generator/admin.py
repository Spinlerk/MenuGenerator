from django.contrib import admin
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
