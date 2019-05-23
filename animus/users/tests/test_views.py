from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from animus.users.tests.factories import UserFactory, UserFactory


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('user-list')
        self.detail_view = 'user-detail'

    def get_detail_url(self, user_id):
        return reverse(self.detail_view, kwargs={'pk': user_id})

    def test_get_list(self):
        """GET the list page of Companies."""
        users = [UserFactory() for i in range(0, 3)]
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_detail_self(self):
          """GET a detail page for a self."""
          response = self.client.get(self.get_detail_url(self.user.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data['first_name'], self.user.first_name)

    def test_get_detail_other(self):
          """GET a detail page for other user."""
          user2 = UserFactory()
          response = self.client.get(self.get_detail_url(user2.id))
          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
