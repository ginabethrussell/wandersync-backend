from django.db import models
from django.utils import timezone

class Itinerary(models.Model):
    title = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    days = models.PositiveIntegerField()
    summary = models.TextField()
    tags = models.JSONField(default=list)  # store list of tags
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
