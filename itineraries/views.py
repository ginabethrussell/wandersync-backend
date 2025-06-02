from rest_framework import viewsets
from .models import Itinerary
from .serializers import ItinerarySerializer

class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all().order_by('-created_at')
    serializer_class = ItinerarySerializer
