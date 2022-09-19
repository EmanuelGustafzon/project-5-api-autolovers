from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Market
from .serializers import MarketSerializer
from carlovers.permissions import IsOwnerOrReadOnly
 
 
class MarketList(generics.ListCreateAPIView):
 
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Market.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
#        'owner__followed__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'brand',
        'model',
        'model_year',
        'country',
        'city',
    ]
 
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
 
 
class MarketDetail(generics.RetrieveUpdateDestroyAPIView):
 
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MarketSerializer
    queryset = Market.objects.all()

