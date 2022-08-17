from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from studenthousing.api import viewsets

route = routers.DefaultRouter()

route.register(r'users', viewsets.UsersViewset, basename='Users')
route.register(r'address', viewsets.AddressViewset, basename='Address')
route.register(r'republics', viewsets.RepublicsViewset, basename='Republics')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
