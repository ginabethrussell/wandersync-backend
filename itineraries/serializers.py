from rest_framework import serializers
from .models import Itinerary, ItineraryItem

class ItineraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryItem
        fields = ["id", "day", "location", "activity", "lodging", "dining", "notes"]

class ItinerarySerializer(serializers.ModelSerializer):
    items = ItineraryItemSerializer(many=True)
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Itinerary
        fields = [
            "id",
            "owner",
            "title",
            "destination",
            "days",
            "summary",
            "recommended_time",
            "tags",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        itinerary = Itinerary.objects.create(owner=self.context["request"].user, **validated_data)
        itinerary = Itinerary.objects.create(**validated_data)
        for item_data in items_data:
            ItineraryItem.objects.create(itinerary=itinerary, **item_data)
        return itinerary
    