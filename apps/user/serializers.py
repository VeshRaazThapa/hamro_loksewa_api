from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import AreasOfPreparations, UserFieldOfInterests,PhoneDirectory
from django.core.exceptions import ValidationError

from .models import UserProfile,UserRole

# login
class CustomTokenObtainPairSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone = attrs.get("phone")
        password = attrs.get("password")


        user = authenticate(phone=phone, password=password)

        try:
            user_profile = UserProfile.objects.get(user=user)
            try:
                user_role = UserRole.objects.get(user=user)
            except UserRole.DoesNotExist:
                user_role=None

            user_profile_data = {
                "id": user_profile.id,
                "user_id": user_profile.user.id,
                "email": user.email,
                "full_name": user_profile.full_name,
                "gender": user_profile.gender,
                "phone": user_profile.phone_directory.phone if user_profile.phone_directory and hasattr(user_profile.phone_directory, 'phone') else None,
                "address": user_profile.address,
                "role": user_role.group.name if user_role else None,
                "dob": user_profile.dob,
                "experience_in_yrs": user_profile.experience_in_yrs,
                "profile_photo_url": user_profile.profile_photo_url.url if user_profile.profile_photo_url and hasattr(user_profile.profile_photo_url, 'url') else None,
                "created_at": user_profile.created_at,
                "updated_at": user_profile.updated_at,
            }
        except UserProfile.DoesNotExist:
            user_profile_data = {}
        response_data={}
        # Add user profile data to the response
        response_data["user_profile"] = user_profile_data
        if not user:
            raise serializers.ValidationError("Invalid phone number or password.")

        refresh = RefreshToken.for_user(user)
        response_data['access'] = str(refresh.access_token)
        response_data['refresh'] = str(refresh)

        return response_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    areas_of_preparation = serializers.ListField(child=serializers.IntegerField(), write_only=True,required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        phone_directory = validated_data.get('phone_directory')
        areas_of_preparation_ids = validated_data.pop('areas_of_preparation', [])

        # If phone_directory is provided, extract the username from it
        if phone_directory:
            username_from_phone = phone_directory.phone

            # Update user_data to include the username from phone directory
            user_data['username'] = username_from_phone

        # Create the user using the updated user_data
        user = UserSerializer().create(user_data)
        user_role = UserRole.objects.create(user=user, group=Group.objects.get(name='Student'))
        print('Created User Role', user_role)
        # Create the user profile with the remaining validated data
        user_profile = UserProfile.objects.create(user=user, **validated_data)

        # Create UserFieldOfInterests entries based on the areas_of_preparation_ids
        for area_id in areas_of_preparation_ids:
            try:
                area_of_preparation = AreasOfPreparations.objects.get(id=area_id)
                UserFieldOfInterests.objects.create(
                    user=user,
                    areas_of_preparation=area_of_preparation
                )
            except AreasOfPreparations.DoesNotExist:
                # Handle the case where the AreasOfPreparations does not exist
                raise serializers.ValidationError(f"Area of preparation with ID {area_id} does not exist.")

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

class PhoneDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneDirectory
        fields = ['phone']

    def validate_phone(self, value):
        if len(value) < 10:
            raise ValidationError("Phone number must be at least 10 digits.")
        return value

class OTPVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

class ForgotPasswordInitiateSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)

class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

# Serializer for AreasOfPreparations
class AreasOfPreparationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasOfPreparations
        fields = ['id', 'name', 'icon', 'created_at', 'updated_at']

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