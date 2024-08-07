from django.contrib.auth.models import User
from django import forms
from .models import UserMainCourse, UserSalad, UserSideDishes, UserSoup, Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "password")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match")

        return cd["password2"]


class UserMainCourseForm(forms.ModelForm):
    class Meta:
        model = UserMainCourse
        fields = ["name", "description"]


class UserSaladForm(forms.ModelForm):
    class Meta:
        model = UserSalad
        fields = ["name", "description"]


class UserSideDishesForm(forms.ModelForm):
    class Meta:
        model = UserSideDishes
        fields = ["name", "description"]


class UserSoupForm(forms.ModelForm):
    class Meta:
        model = UserSoup
        fields = ["name", "description"]


class SideDishForm(forms.ModelForm):
    side_dish = forms.CharField(
        label="Side Dish",
        widget=forms.TextInput(
            attrs={"class": "form-control", list: "side_dishes-list"}
        ),
    )

    class Meta:
        model = UserSideDishes
        fields = ["side_dish"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo"]

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"class": "form-control"}),
        }