from django.urls import path

from rest_framework.routers import DefaultRouter

from animus.users.views import UserViewSet, UserCreateViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

app_name = "users"
urlpatterns = router.urls
