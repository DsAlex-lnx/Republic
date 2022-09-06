from dataclasses import fields
from rest_framework import serializers, validators
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

    class Meta:
        model = Republic
        fields = (
                    'title', 
                    'description', 
                    'price', 
                    'house_type', 
                    'address',
                    'user'
                )
    
        read_only_fields = ('user',)

    def create(self, validated_data):
        request = self.context.get('request')
        
        user_id = request.user.id
        locator = Locator.objects.get(user=user_id)
        
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        
        republic = Republic.objects.create(address=address, user=locator, **validated_data)
        republic.save()
        
        return republic
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        representation = dict()    
        user = Locator.objects.get(id=ret['user']) 

        representation['title'] = ret['title']
        representation['description'] = ret['description']
        representation['price'] = ret['price']
        representation['house_type'] = ret['house_type']
        representation['address'] = ret['address']
       
        if user is not None:
            representation['username'] = user.user.username
            representation['phone'] = user.phone
        else: 
            representation['username'] = ''
            representation['phone'] = ''

        return representation