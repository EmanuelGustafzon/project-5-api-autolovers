from rest_framework import generics, permissions
from carlovers.permissions import IsOwnerOrReadOnly
from commentlikes.models import Commentlikes
from commentlikes.serializers import CommentLikeSerializer


# Like a comment views
class CommentLikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = Commentlikes.objects.all()
 
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
 
 
class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = Commentlikes.objects.all()
