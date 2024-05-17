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
]