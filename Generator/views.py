from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMainCourse, UserSoup, UserSalad, UserSideDishes
from .forms import (
    UserRegistrationForm,
    UserMainCourseForm,
    UserSoupForm,
    UserSaladForm,
    UserSideDishesForm, ProfileEditForm,
)


"""Views for user main courses"""


@login_required
def index(request):
    """Renders the dashboard for logged-in users"""
    return render(request, "dashboard.html")


def register(request):
    form = UserRegistrationForm()
    """
    Handles user registration
    Renders the registration form an process for submission
    Ensures the new user is not admin or superuser
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            """ensuring that the new user is not setup as admin"""
            new_user.is_staff = False
            new_user.is_superuser = False
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()

            return render(request, "account/register_done.html", {"new_user": new_user})

    return render(request, "account/register.html", {"form": form})


@login_required
def user_main_courses(request):
    """
    Displays the main course for the logged in users with pagination
    """
    main_courses = UserMainCourse.objects.filter(user=request.user)

    paginator = Paginator(main_courses, 10)
    page_number = request.GET.get("page", 1)
    try:
        main_courses = paginator.page(page_number)
    except PageNotAnInteger:
        main_courses = paginator.page(1)
    except EmptyPage:
        main_courses = paginator.page(paginator.num_pages)

    return render(
        request,
        "user_database_interface/user_main_courses.html",
        {"main_courses": main_courses},
    )


@login_required
def add_main_course(request):
    """
    Allows the user to add a new main course
    """

    if request.method == "POST":
        form = UserMainCourseForm(request.POST)
        if form.is_valid():
            new_main_course = form.save(commit=False)
            new_main_course.user = request.user
            new_main_course.save()
            return redirect("Generator:main_courses")
    else:
        form = UserMainCourseForm()
    return render(
        request, "user_database_interface/add_main_course.html", {"form": form}
    )


@login_required
def edit_user_main_courses(request, id):
    """
    Allows the user to edit an existing main course
    """

    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    if request.method == "POST":
        form = UserMainCourseForm(request.POST, instance=main_course)
        if form.is_valid():
            form.save()
            return redirect("Generator:main_courses")

    else:
        form = UserMainCourseForm(instance=main_course)
    return render(
        request,
        "user_database_interface/edit_main_course.html",
        {"form": form, "main_course": main_course},
    )


""" delete modal"""


@login_required
def delete_user_main_course(request, id):
    """
    Deletes the main course for the logged in user
    """
    main_course = get_object_or_404(UserMainCourse, id=id, user=request.user)
    main_course.delete()

    return HttpResponse("ok")


""" Views for user soups """


@login_required
def user_soups(request):
    """Displays the soups for the logged in user with pagination"""
    soups = UserSoup.objects.filter(user=request.user)

    paginator = Paginator(soups, 10)
    page_number = request.GET.get("page", 1)
    try:
        soups = paginator.page(page_number)
    except PageNotAnInteger:
        soups = paginator.page(1)
    except EmptyPage:
        soups = paginator.page(paginator.num_pages)

    return render(request, "user_database_interface/user_soups.html", {"soups": soups})


@login_required
def add_user_soup(request):
    """Allows the user to add a new soup"""
    if request.method == "POST":
        form = UserSoupForm(request.POST)
        if form.is_valid():
            new_soup = form.save(commit=False)
            new_soup.user = request.user
            new_soup.save()
            return redirect("Generator:soups")
    else:
        form = UserSoupForm()
    return render(request, "user_database_interface/add_soup.html", {"form": form})


@login_required
def edit_user_soup(request, id):
    """Allows the user to edit an existing soup"""
    soup = get_object_or_404(UserSoup, id=id, user=request.user)
    if request.method == "POST":
        form = UserSoupForm(request.POST, instance=soup)
        if form.is_valid():
            form.save()
            return redirect("Generator:soups")

    else:
        form = UserSoupForm(instance=soup)
    return render(
        request, "user_database_interface/edit_soup.html", {"form": form, "soup": soup}
    )


""" modal delete"""


@login_required
def delete_user_soup(request, id):
    """Allows the user to delete an existing soup"""
    soup = get_object_or_404(UserSoup, id=id, user=request.user)
    soup.delete()

    return HttpResponse("ok")


""" Views for user salads """


@login_required
def user_salads(request):
    """Displays the salads for the logged in user with pagination"""
    salads = UserSalad.objects.filter(user=request.user)

    paginator = Paginator(salads, 10)
    page_number = request.GET.get("page", 1)
    try:
        salads = paginator.page(page_number)
    except PageNotAnInteger:
        salads = paginator.page(1)
    except EmptyPage:
        salads = paginator.page(paginator.num_pages)

    return render(
        request, "user_database_interface/user_salads.html", {"salads": salads}
    )


@login_required
def add_user_salad(request):
    """Allows the user to add a new salad"""
    if request.method == "POST":
        form = UserSaladForm(request.POST)
        if form.is_valid():
            new_salad = form.save(commit=False)
            new_salad.user = request.user
            new_salad.save()
            return redirect("Generator:salads")
    else:
        form = UserSaladForm()
    return render(request, "user_database_interface/add_salad.html", {"form": form})


@login_required
def edit_user_salad(request, id):
    """Allows the user to edit an existing salad"""
    salad = get_object_or_404(UserSalad, id=id, user=request.user)
    if request.method == "POST":
        form = UserSaladForm(request.POST, instance=salad)
        if form.is_valid():
            form.save()
            return redirect("Generator:salads")

    else:
        form = UserSaladForm(instance=salad)
    return render(
        request,
        "user_database_interface/edit_salad.html",
        {"form": form, "salad": salad},
    )


""" modal delete"""


@login_required
def delete_user_salad(request, id):
    """Allows the user to delete an existing salad"""
    salad = get_object_or_404(UserSalad, id=id, user=request.user)
    salad.delete()

    return HttpResponse("ok")


""" Views for user side dishes """


@login_required
def user_side_dishes(request):
    """Displays the side dishes for the logged in user with pagination"""
    side_dishes = UserSideDishes.objects.filter(user=request.user)

    paginator = Paginator(side_dishes, 10)
    page_number = request.GET.get("page", 1)
    try:
        side_dishes = paginator.page(page_number)
    except PageNotAnInteger:
        side_dishes = paginator.page(1)
    except EmptyPage:
        side_dishes = paginator.page(paginator.num_pages)

    return render(
        request,
        "user_database_interface/user_side_dishes.html",
        {"side_dishes": side_dishes},
    )


@login_required
def add_user_side_dish(request):
    """Allows the user to add a new side dish"""
    if request.method == "POST":
        form = UserSideDishesForm(request.POST)
        if form.is_valid():
            new_side_dish = form.save(commit=False)
            new_side_dish.user = request.user
            new_side_dish.save()
            return redirect("Generator:side_dishes")
    else:
        form = UserSideDishesForm()
    return render(request, "user_database_interface/add_side_dish.html", {"form": form})


@login_required
def edit_user_side_dish(request, id):
    """Allows the user to edit an existing side dish"""
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    if request.method == "POST":
        form = UserSideDishesForm(request.POST, instance=side_dish)
        if form.is_valid():
            form.save()
            return redirect("Generator:side_dishes")

    else:
        form = UserSideDishesForm(instance=side_dish)
    return render(
        request,
        "user_database_interface/edit_side_dish.html",
        {"form": form, "side_dish": side_dish},
    )


""" view for modal delete"""


@login_required
def delete_user_side_dish(request, id):
    """Allows the user to delete an existing side dish"""
    side_dish = get_object_or_404(UserSideDishes, id=id, user=request.user)
    side_dish.delete()

    return HttpResponse("ok")





@login_required
def create_daily_menu(request):
    """view for Daily menu"""
    if request.method == "POST":
        # Processing of the submitted form
        today = timezone.now()
        soup_name = request.POST.get("soup")
        main_course_1_name = request.POST.get("main_course_1")
        main_course_2_name = request.POST.get("main_course_2")
        side_dish_1_name = request.POST.get("side_dish_1")
        side_dish_2_name = request.POST.get("side_dish_2")
        salad_name = request.POST.get("salad")

        """ If the item doesn't exist in database, it will be created and added to the database '"""
        # Updating last used date or creating soup
        if soup_name:
            soup, created = UserSoup.objects.get_or_create(
                name=soup_name, user=request.user
            )
            soup.last_used = today
            soup.save()
        else:
            soup = None  # if item would not be inputted it will be set up as none

        # Updating last used date or creating main dishes and side dishes
        main_courses = []
        if main_course_1_name:
            main_course_1, created = UserMainCourse.objects.get_or_create(
                name=main_course_1_name, user=request.user
            )
            main_course_1.last_used = today
            main_course_1.save()
            main_courses.append(main_course_1)

        if main_course_2_name:
            main_course_2, created = UserMainCourse.objects.get_or_create(
                name=main_course_2_name, user=request.user
            )
            main_course_2.last_used = today
            main_course_2.save()
            main_courses.append(main_course_2)

        # Updating last used date or creating salad
        if salad_name:
            salad, created = UserSalad.objects.get_or_create(
                name=salad_name, user=request.user
            )
            salad.last_used = today
            salad.save()
        else:
            salad = None  # if item would not be inputted it will be set up as none

        main_courses_with_dishes = []
        side_dishes = [side_dish_1_name, side_dish_2_name]

        for index, main_course in enumerate(main_courses):
            # going through main courses list,
            # the index variable is used to track the order of the main courses in the list.
            text = main_course.name

            if index < len(side_dishes):
                # Checks if the current index is less than the length of the side_dishes list.
                if side_dishes[index] == "":
                    text = f"{text} {side_dishes[index]}"
                else:
                    text = f"{text}, {side_dishes[index]}"

            main_courses_with_dishes.append(text)

        context = {
            "soup": soup,
            "main_courses_with_dishes": main_courses_with_dishes,
            "salad": salad,
        }

        return render(request, "daily_menu_complete.html", context)

    """Default view - generating the longest unused dishes"""
    soup = UserSoup.objects.filter(
        last_used__isnull=True
    ).first()  # taking the never used soup or last used soup
    if not soup:
        soup = UserSoup.objects.order_by("last_used").first()

    main_courses = list(
        UserMainCourse.objects.filter(last_used__isnull=True)[:2]
    )  # gets and stores up to 2 instances
    if len(main_courses) < 2:  # check if main curses list contains less than 2 items
        additional_courses = list(
            UserMainCourse.objects.order_by("last_used")[: 2 - len(main_courses)]
            # if main_courses has less than 2 entries, it gets additional courses.
        )
        main_courses.extend(additional_courses)

    salad = UserSalad.objects.filter(
        last_used__isnull=True
    ).first()  # taking the never used soup or last used salad
    if not salad:
        salad = UserSalad.objects.order_by("last_used").first()

    side_dishes = UserSideDishes.objects.all()

    context = {
        "soup": soup,
        "main_courses": main_courses,
        "salad": salad,
        "side_dishes": side_dishes,
        "soups": UserSoup.objects.all(),
        "main_courses_list": UserMainCourse.objects.all(),
        "salads": UserSalad.objects.all(),
    }

    return render(request, "daily_menu.html", context)


class CustomLoginView(LoginView):
    """Custom login view to redirect authenticated users to dashboard if they try to go to login page"""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("Generator:dashboard")
        return super().dispatch(request, *args, **kwargs)



def user_list(request):
    users = User.objects.select_related('profile').all()
    return render(request, 'user_list.html', {"users": users})

def user_detail(request, id):
    user = get_object_or_404(User.objects.select_related('profile'), id=id)

    if request.method == 'POST':
        profile_form = ProfileEditForm(
            instance=user.profile,
            data=request.POST,
            files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileEditForm(instance=user.profile)

    return render(request, 'user_detail.html', {"profile_form": profile_form})