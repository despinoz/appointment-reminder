from rest_framework import viewsets, permissions

from animus.patients.models import Patient
from animus.patients.api import serializers


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Patient class"""

    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer
