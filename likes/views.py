from rest_framework import generics, permissions
from carlovers.permissions import IsOwnerOrReadOnly
from likes.models import Reviewlikes
from likes.serializers import ReviewLikeSerializer

# Like a review views
class ReviewLikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReviewLikeSerializer
    queryset = Reviewlikes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewLikeSerializer
    queryset = Reviewlikes.objects.all()


