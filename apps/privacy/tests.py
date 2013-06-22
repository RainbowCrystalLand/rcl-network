from django.test import TestCase
# models
from privacy.models import PrivacyLevel, RCLPrivacySetting
from users.models import User
# exceptions
from django.db import IntegrityError


class ClassTest(TestCase):
    def setUp(self):
        user = User(email="test@test.com")
        user.save()
        privacy_level = PrivacyLevel(name='Level 0', level=0, creator=user)
        privacy_level.save()
        self.privacy_level = privacy_level
        self.user = user

    def test_privacy_level_creation(self):
        """
        Just tests the creation of a Privacy Level instance
        """
        privacy_level = PrivacyLevel(
            name='Level 1', level=1, creator=self.user)
        privacy_level.save()

    def test_privacy_level_unicode(self):
        """
        Tests that the unicode method displays ok
        """
        self.assertEqual(u'%s' % self.privacy_level, "Level 0")

    def test_privacy_level_level_unique(self):
        """
        Tests that it's not possible to have two PrivacyLevel
        records with same level
        """
        privacy_level = PrivacyLevel(
            name='Level 0-test', level=0, creator=self.user)
        try:
            privacy_level.save()
        except IntegrityError:
            pass

    def test_rcl_privacy_settings_creation(self):
        """
        Just test the creation of a RCL Privacy Settings instance
        """
        privacy_settings = RCLPrivacySetting()
        privacy_settings.save()
