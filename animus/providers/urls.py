from rest_framework.routers import DefaultRouter

from animus.providers.api.viewsets import ProviderViewSet

app_name = "patients"
router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
