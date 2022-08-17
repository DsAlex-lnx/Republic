from django.db import models
from uuid import uuid4

class Address(models.Model):
    id_address = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    house_number = models.IntegerField()
    zip_code = models.CharField(max_length=9)

    def __str__(self):
        return self.street

class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    phone = models.CharField(max_length=11, unique=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Republic(models.Model):
    id_republic = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)
    description = models.CharField(max_length=255)
    house_type = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='republics')
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title