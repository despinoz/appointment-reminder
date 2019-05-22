from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from animus.users.permissions import IsUser
from animus.users.api.serializers import CreateUserSerializer, UserSerializer


User = get_user_model()

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUser,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
