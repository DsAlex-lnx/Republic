from rest_framework import serializers
from studenthousing.models import User, Address, Republic

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class RepublicSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    address_street = serializers.CharField(source='address.street', read_only=True)
    address_district = serializers.CharField(source='address.district', read_only=True)
    class Meta:
        model = Republic
        fields = (  'id_republic',
                    'title', 
                    'description', 
                    'price', 
                    'house_type', 
                    'user_name', 
                    'user_phone', 
                    'address_street',
                    'address_district'
                )

class UserSerializer(serializers.ModelSerializer):
    republics = RepublicSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (  'id_user',
                    'name', 
                    'phone', 
                    'email', 
                    'password', 
                    'republics'
                )
