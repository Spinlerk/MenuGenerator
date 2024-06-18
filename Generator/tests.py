from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import UserSoup, UserMainCourse, UserSalad, UserSideDishes
from django.urls import reverse
from Generator.forms import (
    UserMainCourseForm,
    UserSaladForm,
    UserSideDishesForm,
    UserSoupForm,
    UserRegistrationForm,
)

"""Tests for user model creation and its properties"""


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user for testing"""
        new_user = User(username="testuser", email="test@gmail.com")
        new_user.set_password("test123456")
        new_user.save()

    def test_user_creation(self):
        """Verify the user was created correctly"""
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.check_password("test123456"))

    def test_user_str_representation(self):
        """Verify the string representation of the user"""
        user = User.objects.get(username="testuser")
        self.assertEqual(str(user), "testuser")


"""Test for verifying the signal for profile creation"""

User = get_user_model()


class TestUserSignals(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing signals
        cls.user = User.objects.create_user(
            username="testuser", email="test@gmail.com", password="test123456"
        )

    def test_user_creation_signal(self):
        # Ensure the signal was triggered and the profile was created
        self.assertTrue(hasattr(self.user, "profile"))
        self.assertEqual(self.user.profile.user, self.user)


"""Test fof verifying models and their relationship"""


class MenuModelsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", email="test@gmail.com", password="12345"
        )

        # Create menu items with the user
        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(
            name="Grilled Chicken", user=self.user
        )
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSalad.objects.create(name="French fries", user=self.user)

    def test_soup_creation(self):
        # verifying the soup item was created correctly
        soup = UserSoup.objects.get(name="Tomato Soup")
        self.assertEqual(soup.name, "Tomato Soup")

    def test_main_course_creation(self):
        # Verifying the main course item was created correctly
        main_course = UserMainCourse.objects.get(name="Grilled Chicken")
        self.assertEqual(main_course.name, "Grilled Chicken")

    def test_salad_creation(self):
        # Verifying the salad item was created correctly
        salad = UserSalad.objects.get(name="Caesar Salad")
        self.assertEqual(salad.name, "Caesar Salad")

    def test_side_dish_creation(self):
        # Verifying the side dish item was created correctly
        side_dish = UserSalad.objects.get(name="French fries")
        self.assertEqual(side_dish.name, "French fries")

    def test_user_association(
        self,
    ):  # testing if data are correctly assigned to the user who created them.
        self.assertEqual(self.soup.user.username, "testuser")
        self.assertEqual(self.main_course.user.username, "testuser")
        self.assertEqual(self.salad.user.username, "testuser")


"""Tests creation of various menu items (soup, main course, salad, side dishes)."""


class MenuViewsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", email="test@gmail.com", password="12345"
        )

        # Log in the user
        self.client.login(username="testuser", password="12345")

        # Create menu items associated with the user
        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(
            name="Grilled Chicken", user=self.user
        )
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSideDishes.objects.create(
            name="French fries", user=self.user
        )
        """Tests the GET and POST requests for creating a daily menu."""

    def test_create_daily_menu_view_get(self):
        # Test get request to create daily menu view
        response = self.client.get(reverse("Generator:create_daily_menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "daily_menu.html")

    def test_create_daily_menu_view_post(self):
        # Test the post request to create daily menu request
        data = {
            "soup": "Tomato Soup",
            "main_course_1": "Grilled Chicken",
            "salad": "Caesar Salad",
            "side_dish": "French fries",
        }
        response = self.client.post(reverse("Generator:create_daily_menu"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "daily_menu_complete.html")


"""Verifies the validity of forms for creating various menu items."""


# Test verifying forms related to user menu items
class TestUserMainCourseForm(TestCase):

    def test_valid_form(self):
        # Test form validation with valid data
        form_data = {
            "name": "Pasta Carbonara",
            "description": "Delicious pasta with creamy sauce",
        }
        form = UserMainCourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        # Test form validation with blank data
        form = UserMainCourseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])


class TestUserSaladForm(TestCase):

    def test_valid_form(self):
        form_data = {
            "name": "Caesar Salad",
            "description": "Classic Caesar salad with chicken",
        }
        form = UserSaladForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = UserSaladForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])


class TestUserSideDishesForm(TestCase):

    def test_valid_form(self):
        # Test form validation with walid data
        form_data = {
            "name": "Mashed Potatoes",
            "description": "Creamy mashed potatoes with butter",
        }
        form = UserSideDishesForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        # Test form validation with blank data
        form = UserSideDishesForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])


class TestUserSoupForm(TestCase):

    def test_valid_form(self):
        # Test form validation with walid data
        form_data = {
            "name": "Tomato Soup",
            "description": "Homemade tomato soup with fresh basil",
        }
        form = UserSoupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        # Test form validation with blank data
        form = UserSoupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])


"""Checks the content of the daily menu template to"""


class MenuTemplatesTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", email="test@gmail.com", password="12345"
        )

        # Log in the user
        self.client.login(username="testuser", password="12345")

        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(
            name="Grilled Chicken", user=self.user
        )
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSideDishes.objects.create(
            name="French fries", user=self.user
        )

    def test_daily_menu_template_content(self):
        # Test the content of daily menu template
        response = self.client.get(reverse("Generator:create_daily_menu"))
        self.assertContains(response, "Daily Menu")
        self.assertContains(response, "Tomato Soup")
        self.assertContains(response, "Grilled Chicken")
        self.assertContains(response, "Caesar Salad")
        self.assertContains(response, "French fries")


class TestViews(TestCase):

    def setUp(self):
        """Setup method to create a client and a test user"""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_index_view(self):
        """Test to verify the dashboard view loads correctly"""
        response = self.client.get(reverse("Generator:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")

    def test_register_view_get(self):
        """Test to verify the GET request for the register view"""
        response = self.client.get(reverse("Generator:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/register.html")
        self.assertIsInstance(response.context["form"], UserRegistrationForm)

    def test_register_view_post_valid(self):
        """Test to verify the POST request for the register view with valid data"""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "password": "newpassword",
            "password2": "newpassword",
        }
        response = self.client.post(reverse("Generator:register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/register_done.html")
        self.assertIsInstance(response.context["new_user"], User)

    def test_user_main_courses_view(self):
        """Test to verify the main courses view for a user"""
        UserMainCourse.objects.create(name="Course 1", user=self.user)
        UserMainCourse.objects.create(name="Course 2", user=self.user)

        response = self.client.get(reverse("Generator:main_courses"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "user_database_interface/user_main_courses.html"
        )
        self.assertEqual(len(response.context["main_courses"]), 2)

    def test_add_main_course_view_get(self):
        """Test to verify the GET request for adding a main cour"""
        response = self.client.get(reverse("Generator:add_main_course"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "user_database_interface/add_main_course.html"
        )
        self.assertIsInstance(response.context["form"], UserMainCourseForm)

    def test_add_main_course_view_post_valid(self):
        """Test to verify the POST request for adding a main course with valid data"""
        data = {"name": "New Course", "description": "Description of new course"}
        response = self.client.post(reverse("Generator:add_main_course"), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(UserMainCourse.objects.filter(name="New Course").count(), 1)

    def test_edit_user_main_course_view_post_valid(self):
        """Test to verify the POST request for editing a main course with valid data"""
        course = UserMainCourse.objects.create(name="Course", user=self.user)
        data = {"name": "Edited Course", "description": "Edited description"}
        response = self.client.post(
            reverse("Generator:edit_main_course", args=[course.id]), data
        )
        self.assertEqual(response.status_code, 302)  # Should redirect
        course.refresh_from_db()
        self.assertEqual(course.name, "Edited Course")

    def test_user_soups_view(self):
        """Test to verify the soups view for a user"""
        UserSoup.objects.create(name="Soup 1", user=self.user)
        UserSoup.objects.create(name="Soup 2", user=self.user)

        response = self.client.get(reverse("Generator:soups"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_database_interface/user_soups.html")
        self.assertEqual(len(response.context["soups"]), 2)
