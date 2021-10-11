from rest_framework import fields, serializers
from . import models
from django.contrib.auth.models import User
class ProductList(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'

class UserSerializer():

     class Meta:
         model = User
         fields = ['id', 'username']