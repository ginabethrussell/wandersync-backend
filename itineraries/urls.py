from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ItineraryViewSet
from .views import RegisterUserView

router = DefaultRouter()
router.register(r'itineraries', ItineraryViewSet, basename='itinerary')

urlpatterns = [
    path('', include(router.urls)),
    path("auth/token/", obtain_auth_token),
    path("auth/register/", RegisterUserView.as_view()),
]
