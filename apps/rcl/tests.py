from django.test import TestCase
# models
from rcl.models import Community, CommunityExperience
from users.models import User
# exceptions
from django.db import IntegrityError


class ClassTest(TestCase):
    def setUp(self):
        u = User(email='test@test.com')
        u.save()
        self.user = u
        c = Community(url_name='test-url-setup')
        c.save()
        self.community = c

    def test_community_creation_minimum_info(self):
        """
        Just creates a Community with some information and
        saves the instance.
        """
        c = Community(
            name='Test',
            kind=Community.LAND,
            url_name='test-url'
        )
        c.save()

    def test_community_url_name_unique(self):
        """
        Tries to save a Community without name, checks it's not possible
        """
        c = Community(url_name='test-url')
        c.save()
        c = Community(url_name='test-url')
        try:
            c.save()
        except IntegrityError:
            pass

    def test_community_experience(self):
        ce = CommunityExperience(user=self.user, community=self.community)
        ce.save()