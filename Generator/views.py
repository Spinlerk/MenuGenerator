from django.forms import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMainCourse, UserSoup, UserSalad, UserSideDishes
from .forms import UserRegistrationForm, UserMainCourseForm, UserSoupForm, UserSaladForm, UserSideDishesForm
from django.contrib.auth.views import LoginView

""" Soup """

# Tady jenom ty views k tem polevkam

""" Main course """

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

    paginator = Paginator(main_courses, 10)
    page_number = request.GET.get('page', 1)
    try:
        main_courses = paginator.page(page_number)
    except PageNotAnInteger:
        main_courses = paginator.page(1)
    except EmptyPage:
        main_courses = paginator.page(paginator.num_pages)

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
            return redirect('Generator:soups')
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
    return render(request, 'user_database_interface/edit_side_dish.html', {
        'form': form,
        'side_dish': side_dish
    })


""" prepared delete for modal"""

@login_required
def delete_user_side_dish(request, id):
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    side_dish.delete()

    return HttpResponse("ok")

@login_required
def create_daily_menu(request):
    if request.method == 'POST':
        # Zpracování odeslaného formuláře
        today = timezone.now()
        soup_name = request.POST.get('soup')
        main_course_1_name = request.POST.get('main_course_1')
        main_course_2_name = request.POST.get('main_course_2')
        side_dish_1_name = request.POST.get('side_dish_1')
        side_dish_2_name = request.POST.get('side_dish_2')
        salad_name = request.POST.get('salad')

        # Aktualizace nebo vytvoření polévky
        if soup_name:
            soup, created = UserSoup.objects.get_or_create(name=soup_name)
            soup.last_used = today
            soup.save()
        else:
            soup = None

        # Aktualizace nebo vytvoření hlavních chodů a příloh
        main_courses = []
        if main_course_1_name:
            main_course_1, created = UserMainCourse.objects.get_or_create(name=main_course_1_name)
            main_course_1.last_used = today
            main_course_1.save()
            main_courses.append(main_course_1)

        if main_course_2_name:
            main_course_2, created = UserMainCourse.objects.get_or_create(name=main_course_2_name)
            main_course_2.last_used = today
            main_course_2.save()
            main_courses.append(main_course_2)

        # Aktualizace nebo vytvoření salátu
        if salad_name:
            salad, created = UserSalad.objects.get_or_create(name=salad_name)
            salad.last_used = today
            salad.save()
        else:
            salad = None

        # print(side_dish_1_name)
        # print(side_dish_2_name)
        #
        # print([model_to_dict(main_course) for main_course in main_courses])
        # print(main_courses.values())

        main_courses_with_dishes = []
        side_dishes = [side_dish_1_name, side_dish_2_name]

        for index, main_course in enumerate(main_courses):
            text = main_course.name

            if index < len(side_dishes):
                text = f"{text}, {side_dishes[index]}"

            main_courses_with_dishes.append(text)

        context = {
            'soup': soup,
            # 'main_courses': main_courses,
            'main_courses_with_dishes': main_courses_with_dishes,
            'salad': salad,
            # 'side_dishes': [side_dish_1_name, side_dish_2_name]
        }

        return render(request, 'daily_menu_complete.html', context)

    # Výchozí zobrazení - vygenerování nejdéle nepoužitých jídel
    soup = UserSoup.objects.filter(last_used__isnull=True).first()
    if not soup:
        soup = UserSoup.objects.order_by('last_used').first()

    main_courses = list(UserMainCourse.objects.filter(last_used__isnull=True)[:2])
    if len(main_courses) < 2:
        additional_courses = list(UserMainCourse.objects.order_by('last_used')[:2 - len(main_courses)])
        main_courses.extend(additional_courses)

    salad = UserSalad.objects.filter(last_used__isnull=True).first()
    if not salad:
        salad = UserSalad.objects.order_by('last_used').first()

    side_dishes = UserSideDishes.objects.all()

    context = {
        'soup': soup,
        'main_courses': main_courses,
        'salad': salad,
        'side_dishes': side_dishes,
        'soups': UserSoup.objects.all(),
        'main_courses_list': UserMainCourse.objects.all(),
        'salads': UserSalad.objects.all()
    }

    return render(request, 'daily_menu.html', context)

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Generator:dashboard')
        return super().dispatch(request, *args, **kwargs)