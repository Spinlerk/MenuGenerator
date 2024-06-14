from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserSoup, UserMainCourse, UserSalad,UserSideDishes
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from Generator.forms import UserMainCourseForm, UserSaladForm, UserSideDishesForm, UserSoupForm
from Generator.models import Profile


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_user = User(username='testuser',
                        email='test@gmail.com')
        new_user.set_password('test123456')
        new_user.save()

    def test_user_creation(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.check_password('test123456'))

    def test_user_str_representation(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(str(user), 'testuser')


"""Tests below are assembled for verification if database has been created when user is created"""

User = get_user_model()

class TestUserSignals(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing signals
        cls.user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='test123456'
        )

    def test_user_creation_signal(self):
        # Ensure the signal was triggered and the profile was created
        self.assertTrue(hasattr(self.user, 'profile'))
        self.assertEqual(self.user.profile.user, self.user)



"""Checking if models working right"""

class MenuModelsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='12345')

        # Create menu items with the user
        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(name="Grilled Chicken", user=self.user)
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSalad.objects.create(name="French fries", user=self.user)

    def test_soup_creation(self):
        soup = UserSoup.objects.get(name="Tomato Soup")
        self.assertEqual(soup.name, "Tomato Soup")

    def test_main_course_creation(self):
        main_course = UserMainCourse.objects.get(name="Grilled Chicken")
        self.assertEqual(main_course.name, "Grilled Chicken")

    def test_salad_creation(self):
        salad = UserSalad.objects.get(name="Caesar Salad")
        self.assertEqual(salad.name, "Caesar Salad")

    def test_side_dish_creation(self):
        side_dish = UserSalad.objects.get(name="French fries")
        self.assertEqual(side_dish.name, "French fries")

    def test_user_association(self): #testing if data are correctly assigned to the user who created them.
        self.assertEqual(self.soup.user.username, 'testuser')
        self.assertEqual(self.main_course.user.username, 'testuser')
        self.assertEqual(self.salad.user.username, 'testuser')


"""checking if views working properly"""
class MenuViewsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='12345')

        # Log in the user
        self.client.login(username='testuser', password='12345')

        # Create menu items associated with the user
        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(name="Grilled Chicken", user=self.user)
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSideDishes.objects.create(name="French fries", user=self.user)

    def test_create_daily_menu_view_get(self):
        response = self.client.get(reverse('Generator:create_daily_menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'daily_menu.html')

    def test_create_daily_menu_view_post(self):
        data = {
            'soup': 'Tomato Soup',
            'main_course_1': 'Grilled Chicken',
            'salad': 'Caesar Salad',
            'side_dish': 'French fries',
        }
        response = self.client.post(reverse('Generator:create_daily_menu'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'daily_menu_complete.html')


"""Form tests"""

class TestUserMainCourseForm(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'Pasta Carbonara',
            'description': 'Delicious pasta with creamy sauce'
        }
        form = UserMainCourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = UserMainCourseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])


class TestUserSaladForm(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'Caesar Salad',
            'description': 'Classic Caesar salad with chicken'
        }
        form = UserSaladForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = UserSaladForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])


class TestUserSideDishesForm(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'Mashed Potatoes',
            'description': 'Creamy mashed potatoes with butter'
        }
        form = UserSideDishesForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = UserSideDishesForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])


class TestUserSoupForm(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'Tomato Soup',
            'description': 'Homemade tomato soup with fresh basil'
        }
        form = UserSoupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = UserSoupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

class MenuTemplatesTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='12345')

        # Log in the user
        self.client.login(username='testuser', password='12345')

        self.soup = UserSoup.objects.create(name="Tomato Soup", user=self.user)
        self.main_course = UserMainCourse.objects.create(name="Grilled Chicken", user=self.user)
        self.salad = UserSalad.objects.create(name="Caesar Salad", user=self.user)
        self.side_dish = UserSideDishes.objects.create(name="French fries", user=self.user)

    def test_daily_menu_template_content(self):
        response = self.client.get(reverse('Generator:create_daily_menu'))
        self.assertContains(response, 'Daily Menu')
        self.assertContains(response, 'Tomato Soup')
        self.assertContains(response, 'Grilled Chicken')
        self.assertContains(response, 'Caesar Salad')
        self.assertContains(response, 'French fries')