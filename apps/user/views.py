from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view,OpenApiExample
from .models import UserProfile,UserRole,AreasOfPreparations,UserFieldOfInterests
from .serializers import UserProfileSerializer,UserRoleSerializer,AreasOfPreparationsSerializer,UserFieldOfInterestsSerializer,PhoneDirectorySerializer, OTPVerificationSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile,PhoneDirectory
from rest_framework import status, views
from rest_framework_simplejwt.views import TokenObtainPairView

import random


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@extend_schema_view(
    list=extend_schema(summary="List all users",description="Retrieve list of user profiles"),
    retrieve=extend_schema(summary="Get a single user profile",description="Retrieve a single user profile"),
    create=extend_schema(summary="Register a new user",description="Create a new user profile"),
    update=extend_schema(summary="Update a User Profile",description="Update a user profile"),
    partial_update=extend_schema(summary="Partially update a user profile",description="Partially update a user profile"),
    destroy=extend_schema(summary="Delete a user profile",description="Delete a user profile")
)
@permission_classes([AllowAny])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@extend_schema_view(
    list=extend_schema(description="Retrieve list of user roles"),
    retrieve=extend_schema(description="Retrieve a single user role"),
    create=extend_schema(description="Create a new user role"),
    update=extend_schema(description="Update a user role"),
    partial_update=extend_schema(description="Partially update a user role"),
    destroy=extend_schema(description="Delete a user role")
)
@permission_classes([AllowAny])
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    def perform_create(self, serializer):
        # You can add custom logic for creating the UserRole here
        serializer.save()

    def perform_update(self, serializer):
        # You can add custom logic for updating the UserRole here
        serializer.save()

    def perform_destroy(self, instance):
        # Custom logic for deletion can be added here
        instance.delete()

@extend_schema(
    request=PhoneDirectorySerializer,
    responses={
        200: OpenApiExample(
            "OTP sent successfully",
            value={"message": "OTP sent.", "otp": "123456"},
            status_codes=["200"]
        ),
        404: OpenApiExample(
            "Phone number not found",
            value={"detail": "Phone number not found."},
            status_codes=["404"]
        ),
        400: OpenApiExample(
            "Phone number already exists",
            value={"detail": "Phone number already exists."},
            status_codes=["400"]
        )
    }
)
class SendOTPView(APIView):
    """
    View to send OTP for phone verification (simulated).
    """
    def post(self, request):
        phone = request.data.get('phone')

        # Check if the phone number already exists
        existing_phone = PhoneDirectory.objects.filter(phone=phone).first()
        if existing_phone and existing_phone.is_verified:
                return Response({"detail": "Phone number is already verified","phone_directory_id":existing_phone.id}, status=status.HTTP_400_BAD_REQUEST)
        if not existing_phone:
            # Create a new entry if the phone number does not exist
            phone_directory = PhoneDirectory.objects.create(phone=phone, is_verified=False)

            # Save the dummy OTP (123456) to the PhoneDirectory model
            # TODO: add otp field in phone directory
            # phone_directory.otp = "123456"  # Assuming 'otp' is a field in the PhoneDirectory model
            phone_directory.save()

        # Return the dummy OTP response
        return Response({"message": "OTP sent.", "otp": "123456"}, status=status.HTTP_200_OK)

@extend_schema(
    request=OTPVerificationSerializer,
    responses={
        200: OpenApiExample(
            "Phone number verified successfully",
            value={"message": "Phone number verified successfully."},
            status_codes=["200"]
        ),
        400: OpenApiExample(
            "Invalid OTP",
            value={"detail": "Invalid OTP."},
            status_codes=["400"]
        ),
        404: OpenApiExample(
            "Phone number not found",
            value={"detail": "Phone number not found."},
            status_codes=["404"]
        )
    }
)
class VerifyOTPView(APIView):
    """
    View to verify OTP.
    """
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone')
            otp = serializer.validated_data.get('otp')


            if otp == '123456':
                try:
                    phone_directory = PhoneDirectory.objects.get(phone=phone)
                    phone_directory.is_verified = True
                    phone_directory.save()
                    return Response({
                        "message": "Phone number verified successfully.",
                        "phone_directory_id": phone_directory.id
                    }, status=status.HTTP_200_OK)
                except PhoneDirectory.DoesNotExist:
                    return Response({"detail": "Phone number not found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"detail": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    responses={200: AreasOfPreparationsSerializer(many=True)},
)
class AreasOfPreparationsViewSet(viewsets.ModelViewSet):
    queryset = AreasOfPreparations.objects.all()
    serializer_class = AreasOfPreparationsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()  # You can add custom logic here if needed


# Viewset for UserFieldOfInterests with drf_spectacular schema extension
@extend_schema(
    responses={200: UserFieldOfInterestsSerializer(many=True)},
)
class UserFieldOfInterestsViewSet(viewsets.ModelViewSet):
    queryset = UserFieldOfInterests.objects.all()
    serializer_class = UserFieldOfInterestsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic can be added before save, if needed
        serializer.save()