from concurrent.futures.process import _chain_from_iterable_of_lists
from dataclasses import field, fields
from imp import source_from_cache
from rest_framework import serializers, validators
from rest_framework.response import Response
from studenthousing.models import Locator, Address, Republic
from django.contrib.auth.models import User
from knox.auth import AuthToken


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='locator.phone')
    
    class Meta:
        model = User
        fields = (  'id',
                    'username',
                    'email', 
                    'password', 
                    'phone',
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

class RepublicSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_phone = serializers.CharField(source='user.locator.phone', read_only=True)

    class Meta:
        model = Republic
        fields = (  'title', 
                    'description', 
                    'price', 
                    'house_type', 
                    'address',
                    'user_name',
                    'user_phone'
                )

    def create(self, validated_data):
        request = self.context.get('request')
        
        user_id = request.user.id
        locator = Locator.objects.get(user=user_id)
        
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        
        republic = Republic.objects.create(address=address, user=locator, **validated_data)
        republic.save()
        
        return republic