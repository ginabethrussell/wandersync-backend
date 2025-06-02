from django.contrib import admin
from .models import Itinerary, ItineraryItem

class ItineraryItemInline(admin.TabularInline):
    model = ItineraryItem
    extra = 1

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "days", "recommended_time")
    inlines = [ItineraryItemInline]

@admin.register(ItineraryItem)
class ItineraryItemAdmin(admin.ModelAdmin):
    list_display = ("day", "location", "activity", "lodging", "dining", "notes", "itinerary")
