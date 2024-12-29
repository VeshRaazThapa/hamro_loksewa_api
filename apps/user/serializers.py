from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .models import AreasOfPreparations, UserFieldOfInterests

from .models import UserProfile,UserRole
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile

class UserRoleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # or use 'UserSerializer()' to serialize full user details
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())

    class Meta:
        model = UserRole
        fields = ["id", "user", "group", "started_at", "ended_at"]

    def create(self, validated_data):
        return UserRole.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Handle update logic for UserRole instance
        instance.user = validated_data.get('user', instance.user)
        instance.group = validated_data.get('group', instance.group)
        instance.started_at = validated_data.get('started_at', instance.started_at)
        instance.ended_at = validated_data.get('ended_at', instance.ended_at)
        instance.save()
        return instance

# Serializer for AreasOfPreparations
class AreasOfPreparationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasOfPreparations
        fields = ['id', 'name', 'icon_name', 'created_at', 'updated_at']

# Serializer for UserFieldOfInterests
class UserFieldOfInterestsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    areas_of_preparation = serializers.PrimaryKeyRelatedField(queryset=AreasOfPreparations.objects.all())

    class Meta:
        model = UserFieldOfInterests
        fields = ['id', 'user', 'areas_of_preparation']

    def create(self, validated_data):
        # Directly use the field_of_interest id from validated data
        areas_of_preparation = validated_data.pop('areas_of_preparation')
        areas_of_preparation = UserFieldOfInterests.objects.create(
            user=validated_data['user'],
            areas_of_preparation=areas_of_preparation
        )
        return areas_of_preparation