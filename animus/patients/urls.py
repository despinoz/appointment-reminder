from django.urls import path

from rest_framework.routers import DefaultRouter

from animus.patients.api.viewsets import PatientViewSet

app_name = "patients"
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
