from django.contrib.auth.models import User
from django import forms
from .models import UserMainCourse, UserSalad, UserSideDishes, UserSoup

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")

        return cd['password2']

"""Form for display courses"""


class UserMainCourseForm(forms.ModelForm):
    class Meta:
        model = UserMainCourse
        fields = ['name', 'description']

class UserSaladForm(forms.ModelForm):
    class Meta:
        model = UserSalad
        fields = ['name', 'description']

class UserSideDishesForm(forms.ModelForm):
    class Meta:
        model = UserSideDishes
        fields = ['name', 'description']

class UserSoupForm(forms.ModelForm):
    class Meta:
        model = UserSoup
        fields = ['name', 'description']

"""Form for display Daily menu"""

class DailyMenuForm(forms.Form):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    soup = forms.ModelChoiceField(queryset=UserSoup.objects.all(), required=False)
    main_course = forms.ModelChoiceField(queryset=UserMainCourse.objects.all(), required=False)
    side_dish = forms.ModelChoiceField(queryset=UserSideDishes.objects.all(), required=False)
    salad = forms.ModelChoiceField(queryset=UserSalad.objects.all(), required=False)
