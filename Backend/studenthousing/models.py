from django.db import models
from uuid import uuid4

class Address(models.Model):
    id_address = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    house_number = models.IntegerField()
    zip_code = models.CharField(max_length=9)

    def concatenate(self):
        return str( self.street, 
                    self.district, 
                    self.house_number, 
                    self.city, 
                    self.zip_code
                    )

class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    phone = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

class Republic(models.Model):
    id_republic = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)
    description = models.CharField(max_length=255)
    house_type = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)