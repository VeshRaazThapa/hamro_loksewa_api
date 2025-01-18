from rest_framework import serializers
from .models import (
    Province, Association, PackageCategory, PackageSubCategory,
    Package, UserPackage, Subscription, UserSubscription, Payment,
)
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model


# Serializer for AreasOfPreparations
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name']

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = ['id', 'name']

class PackageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageCategory
        fields = ['id', 'name', 'created_at', 'updated_at']

class PackageSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageSubCategory
        fields = ['id', 'name', 'created_at', 'updated_at']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id', 'title', 'areas_of_preparation', 'category', 
            'sub_category', 'price', 'discount_price', 'duration_in_months',
            'features', 'description', 'created_at', 'updated_at',
            'province', 'association'
        ]

class UserPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPackage
        fields = [
            'id', 'user', 'package', 'payment_id',
            'expiry_at', 'created_at', 'updated_at'
        ]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id', 'name', 'price', 'discount_price',
            'duration_in_months', 'features', 'created_at', 'updated_at'
        ]

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = [
            'id', 'user', 'subscription_type', 'payment_id',
            'status', 'expiry_at', 'created_at', 'updated_at'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id', 'user', 'status', 'method', 'created_at',
            'updated_at', 'package_id', 'subscription_id'
        ]