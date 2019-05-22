from django.test import TestCase

from animus.users.api.serializers import UserSerializer
from animus.users.tests.factories import UserFactory

class UserSerializerTestCase(TestCase):
    def test_model_fields(self):
        """Serializer data matches the User object for each field."""
        user = UserFactory()
        serializer = UserSerializer(user)
        for field_name in [
            'id', 'first_name', 'last_name', 'email'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(user, field_name)
            )
