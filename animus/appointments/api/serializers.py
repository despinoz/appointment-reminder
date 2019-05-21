from rest_framework import serializers

from animus.appointments import models


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Appointment
        fields = (
            'pk', 
            'name', 
            'date', 
            'start_time', 
            'end_time', 
        )
