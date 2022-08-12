from rest_framework import serializers
from studenthousing import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('street', 'district', 'city', 'house_number', 'zip_code')

class RepublicSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    
    class Meta:
        model = models.Republic
        fields = ('title', 'price', 'description', 'house_type', 'user_name')