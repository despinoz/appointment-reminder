from rest_framework import serializers

from animus.appointments import models


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Appointment
        fields = (
            'pk', 
            'provider', 
            'patient',
            'date', 
            'start_time', 
            'end_time', 
        )
