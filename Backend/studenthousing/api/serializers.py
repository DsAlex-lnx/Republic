from rest_framework import serializers
from studenthousing.models import User, Address, Republic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class RepublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Republic
        fields = '__all__'

