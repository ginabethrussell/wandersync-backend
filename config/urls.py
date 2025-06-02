from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from itineraries.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('itineraries.urls')),
]
