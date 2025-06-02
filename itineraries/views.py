from rest_framework import viewsets
from .models import Itinerary
from .serializers import ItinerarySerializer
from django.shortcuts import render

class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all().order_by('-created_at')
    serializer_class = ItinerarySerializer

def home(request):
    return render(request, "home.html")
