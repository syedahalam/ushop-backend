from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['owner', 'name', 'image', 'brand', 'category', 'description', 'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']


class ReviewSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Review
        fields = ['owner', 'name', 'brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']

class OrderSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Order
        fields = ['owner', 'name', 'brand', 'category', 'description', 'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['name', 'brand', 'category', 'description', 'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']
