from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'username',
            'description', 'profileimage', 'favorite_car_brand',
            'experience_with_cars',
        ]