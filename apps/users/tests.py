# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
# models
from users.models import User, UserManager
# forms
from users.forms import UserUpdateForm
# exceptions
from django.db import IntegrityError
from django.contrib.auth.models import SiteProfileNotAvailable
# translation & other utils
from django.core.urlresolvers import reverse


class UserClassTest(TestCase):
    """
    This TestCase tests the creation, integrity and methods of the User model
    """
    def setUp(self):
        """
        Setups a user and tests simple User creation
        """
        u = User(username='test', email='test@test.com', 
            first_name='First', last_name='Last')
        u.save()
        self.user = u

    def test_user_email_uniqueness(self):
        """
        Tests that it's not possible to create Users with same email
        """
        u = User(email='test@test.com')
        try:
            u.save()
        except IntegrityError:
            pass

    def test_username_not_unique(self):
        """
        Tests that it's possible to create Users with same username
        """
        u = User(username='test', email='test_other@test.com')
        try:
            u.save()
        except IntegrityError:
            pass

    def test_user_full_name(self):
        """
        Tests User full name presentation
        """
        self.assertEqual(self.user.get_full_name(), 'First Last')

    def test_user_first_name(self):
        """
        Tests User short name presentation
        """
        self.assertEqual(self.user.get_short_name(), 'First')

    def test_user_get_profile(self):
        """
        Tests User profile, we are not using so exception should raise
        """
        try:
            self.user.get_profile()
        except SiteProfileNotAvailable:
            pass


class UserManagerTest(TestCase):
    """
    Tests the custom UserManager class to ensure that (super)user creation
    is working properly.
    """
    def test_manager_is_as_expected(self):
        """
        Tests that the User manager is indeed UserManager
        """
        self.assertEqual(type(User.objects), UserManager)

    def test_user_creation_ok(self):
        """
        Tests the creation of a simple user
        """
        user = User.objects.create_user(username="test", email="t@test.com", 
            password="test")
        self.assertNotEqual(user.pk, None)

    def test_user_creation_no_email(self):
        try:
            User.objects.create_user(username="test", email="", password="test")
        except ValueError:
            pass

    def test_superuser_creation(self):
        user = User.objects.create_superuser(
            username='test_superuser', email="test@test.com", password="test")
        self.assertNotEqual(user.pk, None)


class UserViewsTest(TestCase):
    """
    This class tests all views related to the User model
    """
    def setUp(self):
        user = User.objects.create_user(username='test', email='test@test.com', 
            password='test')
        self.user = user
        self.client = Client()
        self.update_url = reverse('users:profile-edit')
        self.dashboard_url = reverse('users:dashboard')
        self.login_url = reverse('login')

    def test_user_update_get_not_logged(self):
        """
        Tests that a not authenticated user can't access the profile update url.
        """
        # Make the request
        response = self.client.get(self.update_url)
        # Check that redirects to corresponding url
        self.assertRedirects(response, self.login_url+'?next='+self.update_url)

    def test_user_update_get_logged(self):
        """
        Tests that an authenticated user can access the profile update url, and that 
        the form and the user are in the context.
        """
        self.client.login(username='test@test.com', password='test')
        # Make the request
        response = self.client.get(self.update_url)
        # Check response is OK
        self.assertEqual(response.status_code, 200)
        # Check that form and instance are the correct ones
        self.assertEqual(response.context['object'], self.user)
        self.assertEqual(type(response.context['form']), UserUpdateForm)
        # Check template used
        self.assertTemplateUsed(response, 'users/user_update_form.html')
        self.client.logout()

    def test_user_update_post_logged(self):
        """
        Tests that an authenticated user can make a post request to the profile 
        update url, and that the information is correctly updated.
        """
        self.client.login(username='test@test.com', password='test')
        # Prepare data and post the request
        data = {
            'first_name': 'john',
            'last_name': 'main',
            'biography': 'short test bio'
        }
        response = self.client.post(self.update_url, data)
        # Check that redirects to corresponding url
        self.assertRedirects(response, self.update_url)
        # Reload the user to check changes
        self.user = User.objects.get(pk=self.user.pk)
        # Check that form had effect
        self.assertEqual(self.user.first_name, 'john')
        self.assertEqual(self.user.last_name, 'main')
        self.assertEqual(self.user.biography, 'short test bio')
        self.client.logout()

    def test_user_dashboard_not_logged(self):
        """
        Tests that a not authenticated user can't access the dashboard url and 
        that it's redirected to the login page with the corresponding 'next' 
        argumment.
        """
        # Make the request
        response = self.client.get(self.dashboard_url)
        # Check that redirects to corresponding url
        self.assertRedirects(response,
                             self.login_url+'?next='+self.dashboard_url)

    def test_user_dashboard_logged(self):
        """
        Tests that an authenticated user can access the dashboard url and that 
        the template is the expected.
        """
        self.client.login(username='test@test.com', password='test')
        # Make the request
        response = self.client.get(self.dashboard_url)
        # Check response is OK
        self.assertEqual(response.status_code, 200)
        # Check template used
        self.assertTemplateUsed(response, 'users/dashboard.html')
        self.client.logout()
