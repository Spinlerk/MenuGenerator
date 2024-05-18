from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMainCourse, UserSoup, UserSalad, UserSideDishes
from .forms import UserRegistrationForm, UserMainCourseForm, UserSoupForm, UserSaladForm, UserSideDishesForm


# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard.html')


def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            """ensuring that the new user is not setup as admin"""
            new_user.is_staff = False
            new_user.is_superuser = False
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})

    return render(request, "account/register.html", {'form': form})

@login_required
def user_main_courses(request):
    main_courses = UserMainCourse.objects.filter(user=request.user)
    return render(request, 'user_main_courses.html', {main_courses: main_courses})

@login_required
def add_main_course(request):
    if request.method == 'POST':
        form = UserMainCourseForm(request.POST)
        if form.is_valid():
            new_main_course = form.save(commit=False)
            new_main_course.user = request.user
            new_main_course.save()
            return redirect('user_main_courses')
    else:
        form = UserMainCourseForm()
    return render(request, 'add_main_course.html')

@login_required
def edit_user_main_courses(request, course_id):
    main_course = get_object_or_404(UserMainCourse, id=course_id, user=request.user)
    if request.method == 'POST':
        form = UserMainCourseForm(request.POST, instance=main_course)
        if form.is_valid():
            form.save()
            return redirect('user_main_courses')

    else:
        form = UserMainCourseForm(instance=main_course)
    return render(request, edit_user_main_courses.html, {'form': form})

def delete_user_main_course(request, id):
    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    if request.method == 'POST':
        main_course.delete()
        return redirect('user_main_courses')
    return render(request, 'confirm_delete.html', {'main_course': main_course})