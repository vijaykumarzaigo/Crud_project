from rest_framework import serializers
from.models import crud_model


class crud_serializer(serializers.ModelSerializer):
    class Meta:
        model = crud_model
        fields = 'id', 'name', 'profile_picture', 'country'