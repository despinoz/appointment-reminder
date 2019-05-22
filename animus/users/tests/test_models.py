from django.test import TestCase

from animus.users.models import User
from animus.users.tests.factories import UserFactory


class UserTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        user = UserFactory()
        self.assertEqual(str(user), user.email)
