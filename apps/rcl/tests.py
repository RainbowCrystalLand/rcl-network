from django.test import TestCase
# models
from rcl.models import Community, CommunityExperience
from privacy.models import RCLPrivacySetting
from users.models import User
# exceptions
from django.db import IntegrityError
# others
from django.test.client import Client
from django.core.urlresolvers import reverse


class ClassTest(TestCase):
    def setUp(self):
        u = User(email='test@test.com')
        u.save()
        self.user = u
        ps = RCLPrivacySetting.objects.create()
        c = Community(url_name='test-url-setup', privacy_settings=ps)
        c.save()
        self.community = c

    def test_community_creation_minimum_info(self):
        """
        Just creates a Community with some information and
        saves the instance.
        """
        ps = RCLPrivacySetting.objects.create()
        c = Community(
            name='Test',
            kind=Community.LAND,
            url_name='test-url',
            privacy_settings=ps
        )
        c.save()

    def test_community_url_name_unique(self):
        """
        Tries to save a Community without name, checks it's not possible
        """
        ps = RCLPrivacySetting.objects.create()
        c = Community(url_name='test-url', privacy_settings=ps)
        c.save()
        ps = RCLPrivacySetting.objects.create()
        c = Community(url_name='test-url', privacy_settings=ps)
        try:
            c.save()
        except IntegrityError:
            pass

    def test_community_experience(self):
        ce = CommunityExperience(user=self.user, community=self.community)
        ce.save()


class MainViewsTest(TestCase):
    """
    This class tests all the views that are part of the main RCL site (ie not
    the views of the mini sites).
    """
    def setup(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_history_page(self):
        response = self.client.get(reverse('rcl:main-history'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_dci_page(self):
        response = self.client.get(reverse('rcl:main-dci'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_join_page(self):
        response = self.client.get(reverse('rcl:main-join'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
