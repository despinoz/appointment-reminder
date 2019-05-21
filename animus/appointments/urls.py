from rest_framework.routers import DefaultRouter

from animus.appointments.api.viewsets import AppointmentViewSet

app_name = "appointments"
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
