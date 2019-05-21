from animus.appointments import models
from animus.appointments.api import serializers
from rest_framework import viewsets, permissions


class AppointmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Appointment class"""

    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
