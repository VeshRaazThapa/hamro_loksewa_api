from rest_framework import serializers
from .models import (
    Province, Association, PackageCategory, PackageSubCategory,
    Package, UserPackage, Subscription, UserSubscription, Payment, Ebook
)
from django.contrib.auth.models import User, Group


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
            'province', 'association', 'seo_title', 'seo_description',
            'seo_twitter_card_type', 'seo_card_image','curriculum'
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
        fields = '__all__'

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = [
            'id', 'title', 'author', 'description', 'price', 
            'featured_image', 'file_url',  'seo_title', 'seo_description',
            'seo_twitter_card_type', 'seo_card_image','curriculum',
            'created_at', 'updated_at'
        ]