from rest_framework import permissions, viewsets, generics
from .models import Itinerary
from .serializers import ItinerarySerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # List and Create are allowed (IsAuthenticated is checked separately).
        if view.action in ["list", "create"]:
            return True
        # For retrieve/view, allow any authenticated user AFTER they've created at least one.
        if view.action == "retrieve":
            # We’ll enforce “only view if you have your own itinerary” in the viewset below.
            return True
        # For update/delete, only allow the owner
        return obj.owner == request.user

class ItineraryViewSet(viewsets.ModelViewSet):
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        qs = Itinerary.objects.all().order_by("-created_at")
        # “Prevent viewing itineraries until after one is submitted”:
        # check if this user already has at least one itinerary; if not, return empty.
        if not Itinerary.objects.filter(owner=user).exists():
            return Itinerary.objects.none()
        return qs

    def perform_create(self, serializer):
        # Owner is set inside the serializer’s create(), but you could also do:
        serializer.save(owner=self.request.user)

def home(request):
    return render(request, "home.html")

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
