from rest_framework import serializers, validators
from rest_framework.response import Response
from studenthousing.models import Locator, Address, Republic
from django.contrib.auth.models import User
from knox.auth import AuthToken

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
    phone = serializers.CharField(source='locator.phone')
    
    class Meta:
        model = User
        fields = (  'username',
                    'email', 
                    'password', 
                    'phone',
                    'republics'
                )

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists"
                    )
                ]
            }
        }

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get('username'),
            email = validated_data.get('email'),    
            password = validated_data.get('password'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        _, token = AuthToken.objects.create(user)

        Locator.objects.create(user=user, phone=validated_data['locator']['phone'])

        return user
