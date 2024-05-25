from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMainCourse, UserSoup, UserSalad, UserSideDishes
from .forms import UserRegistrationForm, UserMainCourseForm, UserSoupForm, UserSaladForm, UserSideDishesForm


"""Views for user main courses"""

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
    return render(request, 'user_database_interface/user_main_courses.html', {'main_courses': main_courses})


@login_required
def add_main_course(request):
    if request.method == 'POST':
        form = UserMainCourseForm(request.POST)
        if form.is_valid():
            new_main_course = form.save(commit=False)
            new_main_course.user = request.user
            new_main_course.save()
            return redirect('Generator:main_courses')
    else:
        form = UserMainCourseForm()
    return render(request, 'user_database_interface/add_main_course.html', {'form': form})


@login_required
def edit_user_main_courses(request, id):
    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    if request.method == 'POST':
        form = UserMainCourseForm(request.POST, instance=main_course)
        if form.is_valid():
            form.save()
            return redirect('Generator:main_courses')

    else:
        form = UserMainCourseForm(instance=main_course)
    return render(request, 'user_database_interface/edit_main_course.html', {
                    'form': form,
                    'main_course': main_course
    })


""" delete modal"""

@login_required
def delete_user_main_course(request, id):
    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    main_course.delete()

    return HttpResponse("ok")

""" Views for user soups """

@login_required
def user_soups(request):
    soups = UserSoup.objects.filter(user=request.user)
    return render(request, 'user_database_interface/user_soups.html', {'soups': soups})


@login_required
def add_user_soup(request):
    if request.method == 'POST':
        form = UserSoupForm(request.POST)
        if form.is_valid():
            new_soup = form.save(commit=False)
            new_soup.user = request.user
            new_soup.save()
            return redirect('Generator:user_soups')
    else:
        form = UserSoupForm()
    return render(request, 'user_database_interface/add_soup.html',{'form': form})


@login_required
def edit_user_soup(request, id):
    soup = get_object_or_404(UserSoup, id=id, user=request.user)
    if request.method == 'POST':
        form = UserSoupForm(request.POST, instance=soup)
        if form.is_valid():
            form.save()
            return redirect('Generator:soups')

    else:
        form = UserSoupForm(instance=soup)
    return render(request, 'user_database_interface/edit_soup.html', {
        'form': form,
        'soup': soup
    })


""" prepared delete for modal"""

@login_required
def delete_user_soup(request, id):
    soup = get_object_or_404(UserSoup, id=id, user=request.user)
    soup.delete()

    return HttpResponse("ok")


""" Views for user salads """


@login_required
def user_salads(request):
    salads = UserSalad.objects.filter(user=request.user)
    return render(request, 'user_database_interface/user_salads.html', {'salads': salads})


@login_required
def add_user_salad(request):
    if request.method == 'POST':
        form = UserSaladForm(request.POST)
        if form.is_valid():
            new_salad = form.save(commit=False)
            new_salad.user = request.user
            new_salad.save()
            return redirect('Generator:salads')
    else:
        form = UserSaladForm()
    return render(request, 'user_database_interface/add_salad.html', {'form': form})


@login_required
def edit_user_salad(request, id):
    salad = get_object_or_404(UserSalad, id=id, user=request.user)
    if request.method == 'POST':
        form = UserSaladForm(request.POST, instance=salad)
        if form.is_valid():
            form.save()
            return redirect('Generator:salads')

    else:
        form = UserSaladForm(instance=salad)
    return render(request, 'user_database_interface/edit_salad.html', {
        'form': form,
        'salad': salad
    })


""" prepared delete for modal"""

@login_required
def delete_user_salad(request, id):
    salad = get_object_or_404(UserSalad, id=id, user=request.user)
    salad.delete()

    return HttpResponse("ok")


""" Views for user side dishes """

@login_required
def user_side_dishes(request):
    side_dishes = UserSideDishes.objects.filter(user=request.user)
    return render(request, 'user_database_interface/user_side_dishes.html', {'side_dishes': side_dishes})


@login_required
def add_user_side_dish(request):
    if request.method == 'POST':
        form = UserSideDishesForm(request.POST)
        if form.is_valid():
            new_side_dish = form.save(commit=False)
            new_side_dish.user = request.user
            new_side_dish.save()
            return redirect('Generator:user_side_dishes')
    else:
        form = UserSaladForm()
    return render(request, 'user_database_interface/add_side_dish.html', {'form': form})


@login_required
def edit_user_side_dish(request, id):
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    if request.method == 'POST':
        form = UserSideDishesForm(request.POST, instance=side_dish)
        if form.is_valid():
            form.save()
            return redirect('Generator:user_side_dishes')

    else:
        form = UserSideDishesForm(instance=side_dish)
    return render(request, 'user_database_interface/edit_side_dish.html', {
        'form': form,
        'side_dish': side_dish
    })


# """ prepared delete for modal"""

# @login_required
# def delete_user_main_course(request, id):
#     main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
#     main_course.delete()
#
#     return HttpResponse("ok")

