from django.test import TestCase
# models
from users.models import User, UserManager
# exceptions
from django.db import IntegrityError
from django.contrib.auth.models import SiteProfileNotAvailable


class UserClassTest(TestCase):
    """
    This TestCase tests the creation, integrity and methods of the User model
    """
    def setUp(self):
        """
        Setups a user and tests simple User creation
        """
        u = User(email='test@test.com', first_name='First', last_name='Last')
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
        user = User.objects.create_user(email="t@test.com", password="test")
        self.assertNotEqual(user.pk, None)

    def test_user_creation_no_email(self):
        try:
            User.objects.create_user(email="", password="test")
        except ValueError:
            pass

    def test_superuser_creation(self):
        user = User.objects.create_superuser(
            email="test@test.com", password="test")
        self.assertNotEqual(user.pk, None)
