from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Itinerary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="itineraries")
    title = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    days = models.PositiveIntegerField()
    summary = models.TextField()
    tags = models.JSONField(default=list)
    recommended_time = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ItineraryItem(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='items', on_delete=models.CASCADE)
    day = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    activity = models.TextField(blank=True)
    lodging = models.TextField(blank=True)
    dining = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Day {self.day} - {self.location}"
