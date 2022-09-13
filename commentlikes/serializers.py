from django.db import IntegrityError
from rest_framework import serializers
from commentlikes.models import Commentlikes


class CommentLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
 
    class Meta:
        model = Commentlikes
        fields = ['id', 'created_on', 'owner', 'comment']
 
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
