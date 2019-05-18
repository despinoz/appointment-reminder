from animus.patients import models

from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Patient
        fields = (
            'id', 
            'name', 
            'last_name_1', 
            'last_name_2', 
            'email', 
            'phone', 
            'cellphone', 
            'dni', 
        )
