from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = ('pk', 'email', 'first_name', 'last_name')
