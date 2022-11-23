from rest_framework import serializers
from.models import api_model


class api_serializer(serializers.ModelSerializer):
    class Meta:
        model = api_model
        fields = 'id', 'name', 'profile_picture', 'country'
        extra_kwargs = {
            'name': {'required': True},
            'profile_picture': {'required': True},
            'country': {'required': True},
        }
