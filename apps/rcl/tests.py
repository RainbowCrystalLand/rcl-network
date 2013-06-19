from django.test import TestCase
# models
from rcl.models import Community


class ClassTest(TestCase):
    def test_community_creation_minimum_info(self):
        """
        Just creates a Community with minimum information and
        saves the instance.
        """
        c = Community(
            name='Test',
            kind=Community.LAND,
            url_name='test-url'
        )
        c.save()

    def test_community_name_required(self):
        """
        Tries to save a Community without name, checks it's not possible
        """
        c = Community(
            kind=Community.LAND,
            url_name='test-url'
        )
        c.save()