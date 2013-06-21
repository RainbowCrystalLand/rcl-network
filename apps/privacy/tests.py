from django.test import TestCase
# models
from privacy.models import PrivacyLevel, RCLPrivacySetting


class ClassTest(TestCase):
    def setup(self):
        pl = PrivacyLevel(name='Level 0', level=0)
        pl.save()
        self.pl = pl

    def test_privacy_level_creation(self):
        """
        Just tests the creation of a Privacy Level instance
        """
        pl = PrivacyLevel(name='Level 1', level=1)
        pl.save()

    def test_privacy_level_unicode(self):
        """
        Tests that the unicode method displays ok
        """
        self.assertEqual(u'%s' % self.pl, "Level 0")

    def test_privacy_level_level_unique(self):
        """
        Tests that it's not possible to have two PrivacyLevel
        records with same level
        """
        pl = PrivacyLevel(name='Level 0-test', level=0)
        pl.save()

    def test_rcl_privacy_settings_creation(self):
        """
        Just test the creation of a RCL Privacy Settings instance
        """
        ps = RCLPrivacySetting()
        ps.save()
