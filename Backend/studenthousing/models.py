from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Address(models.Model):
    id_address = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)

    def __str__(self):
        return self.street

class Locator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)
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
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Locator, on_delete=models.CASCADE, related_name='republics', blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


