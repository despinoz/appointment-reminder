from rest_framework import viewsets, permissions

from animus.providers import models
from animus.providers.api import serializers


class ProviderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Provider class"""

    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]
