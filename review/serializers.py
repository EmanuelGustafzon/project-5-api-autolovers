from rest_framework import serializers
from .models import Review
from likes.models import Reviewlikes


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'image size larger then 2mb'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'image width larger then 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'image height larger then 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Reviewlikes.objects.filter(
                owner=user, review=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Review
        fields = [
            'id', 'profile_id', 'owner', 'is_owner', 'profile_image',
            'created_on', 'updated_on', 'brand', 'image',
            'model', 'model_year', 'pros', 'cons', 'like_id'
        ]