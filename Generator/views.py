from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMainCourse, UserSoup, UserSalad, UserSideDishes, DailyMenu
from .forms import UserRegistrationForm, UserMainCourseForm, UserSoupForm, UserSaladForm, UserSideDishesForm, DailyMenuForm
from datetime import timedelta
from collections import defaultdict
from django.utils import timezone

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
    return render(request, 'user_database_interface/edit_main_course.html', {'form': form, 'main_course': main_course})

@login_required
def delete_user_main_course(request, id):
    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    main_course.delete()
    return HttpResponse("ok")

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
            return redirect('Generator:soups')
    else:
        form = UserSoupForm()
    return render(request, 'user_database_interface/add_soup.html', {'form': form})

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
    return render(request, 'user_database_interface/edit_soup.html', {'form': form, 'soup': soup})

@login_required
def delete_user_soup(request, id):
    soup = get_object_or_404(UserSoup, id=id, user=request.user)
    soup.delete()
    return HttpResponse("ok")

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
    return render(request, 'user_database_interface/edit_salad.html', {'form': form, 'salad': salad})

@login_required
def delete_user_salad(request, id):
    salad = get_object_or_404(UserSalad, id=id, user=request.user)
    salad.delete()
    return HttpResponse("ok")

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
            return redirect('Generator:side_dishes')
    else:
        form = UserSideDishesForm()
    return render(request, 'user_database_interface/add_side_dish.html', {'form': form})

@login_required
def edit_user_side_dish(request, id):
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    if request.method == 'POST':
        form = UserSideDishesForm(request.POST, instance=side_dish)
        if form.is_valid():
            form.save()
            return redirect('Generator:side_dishes')
    else:
        form = UserSideDishesForm(instance=side_dish)
    return render(request, 'user_database_interface/edit_side_dish.html', {'form': form, 'side_dish': side_dish})

@login_required
def delete_user_side_dish(request, id):
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    side_dish.delete()
    return HttpResponse("ok")

def get_items(request, item_type):
    if item_type == 'soup':
        items = UserSoup.objects.all().values('id', 'name')
    elif item_type == 'main_course':
        items = UserMainCourse.objects.all().values('id', 'name')
    elif item_type == 'side_dish':
        items = UserSideDishes.objects.all().values('id', 'name')
    elif item_type == 'salad':
        items = UserSalad.objects.all().values('id', 'name')
    else:
        items = []
    return JsonResponse({'items': list(items)})


def get_unused_items():
    # Aktuální datum a čas
    current_time = timezone.now()

    # Seznam nejdéle nepoužitých jídel
    unused_items = {
        'soup': {},
        'main_course': {},
        'salad': {},
        'side_dish': {},
    }

    # Získání nejdéle nepoužitých polévek
    unused_soups = UserSoup.objects.filter(last_used__isnull=False).order_by('last_used')
    for soup in unused_soups:
        unused_items['soup'][soup.id] = soup.last_used

    # Získání nejdéle nepoužitých hlavních jídel
    unused_main_courses = UserMainCourse.objects.filter(last_used__isnull=False).order_by('last_used')
    for main_course in unused_main_courses:
        unused_items['main_course'][main_course.id] = main_course.last_used

    # Získání nejdéle nepoužitých salátů
    unused_salads = UserSalad.objects.filter(last_used__isnull=False).order_by('last_used')
    for salad in unused_salads:
        unused_items['salad'][salad.id] = salad.last_used

    # Získání nejdéle nepoužitých příloh
    unused_side_dishes = UserSideDishes.objects.filter(last_used__isnull=False).order_by('last_used')
    for side_dish in unused_side_dishes:
        unused_items['side_dish'][side_dish.id] = side_dish.last_used

    return unused_items

@login_required
def create_weekly_menu(request):
    # Získání seznamu dní v týdnu (například od pondělí do pátku)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Získání nejdéle nepoužitých jídel
    unused_items = get_unused_items()

    # Vytvoření týdenního menu pro každý den v týdnu
    for day in days_of_week:
        daily_menu = DailyMenu.objects.create(day_of_week=day)

        # Přidání jídel do denního menu na základě typu jídla
        for item_type, items in unused_items.items():
            if item_type == 'soup':
                for soup_id, last_used in items.items():
                    soup = UserSoup.objects.get(id=soup_id)
                    daily_menu.soups.add(soup)

            elif item_type == 'main_course':
                for main_course_id, last_used in items.items():
                    main_course = UserMainCourse.objects.get(id=main_course_id)
                    daily_menu.main_courses.add(main_course)

            elif item_type == 'salad':
                for salad_id, last_used in items.items():
                    salad = UserSalad.objects.get(id=salad_id)
                    daily_menu.salads.add(salad)

            elif item_type == 'side_dish':
                for side_dish_id, last_used in items.items():
                    side_dish = UserSideDishes.objects.get(id=side_dish_id)
                    daily_menu.side_dishes.add(side_dish)

        daily_menu.save()

        return render(request, 'weekly_menu.html', {'selected_items': selected_items})
    else:
        form = DailyMenuForm()
    return render(request, 'create_weekly_menu.html', {'form': form})