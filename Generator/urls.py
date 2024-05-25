from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import path, include, reverse_lazy
from . import views


app_name = 'Generator'

PasswordChangeView.success_url = reverse_lazy("Generator:password_change_done")
PasswordResetView.success_url = reverse_lazy("Generator:password_change_done")
PasswordResetConfirmView.success_url = reverse_lazy("Generator:password_reset_complete")

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("", views.index, name='dashboard'),
    path("register", views.register, name='register'),
    path("main-courses", views.user_main_courses, name='main_courses'),
    path("delete-course/<int:id>", views.delete_user_main_course, name='delete_course'),
    path('edit-course/<int:id>/', views.edit_user_main_courses, name='edit_main_course'),
    path("add-course", views.add_main_course, name='add_main_course'),
    path("soups", views.user_soups, name='user_soups'),
    path("add-soup", views.add_user_soup, name='add_soup'),
    path('edit-soup/<int:id>/', views.edit_user_soup, name='edit_soup'),
    path("delete-soup/<int:id>", views.delete_user_soup, name='delete_soup'),
    # path("salads", views.user_salads, name='salads'),
    # path("side-dishes", views.user_side_dishes, name='side_dishes'),
]