from rest_framework import serializers
from .models import Comment
from commentlikes.models import Commentlikes


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    commentlike_id = serializers.SerializerMethodField()
    commentlikes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_commentlike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            commentlike = Commentlikes.objects.filter(
                owner=user, comment=obj
            ).first()
            return commentlike.id if commentlike else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'profile_id', 'owner', 'is_owner', 'profile_image',
            'created_on', 'updated_on', 'content', 'review', 'commentlike_id',
            'commentlikes_count', 
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    review = serializers.ReadOnlyField(source='review.id')