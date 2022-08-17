from rest_framework import viewsets 
from studenthousing.api import serializers
from studenthousing import models

class UsersViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class AddressViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()

class RepublicsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RepublicSerializer
    queryset = models.Republic.objects.all()