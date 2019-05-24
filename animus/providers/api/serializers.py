from animus.providers import models

from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Provider
        fields = (
            'pk', 
            'name', 
            'last_name_1', 
            'last_name_2', 
            'known_as', 
            'nro_colegiatura', 
            'nro_especialista', 
            'specialty', 
            'other_specialty', 
        )
