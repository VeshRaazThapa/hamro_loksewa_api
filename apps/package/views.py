from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import UserProfile,UserRole,AreasOfPreparations,UserFieldOfInterests
from .serializers import UserProfileSerializer,UserRoleSerializer,AreasOfPreparationsSerializer,UserFieldOfInterestsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import permission_classes

@extend_schema_view(
    list=extend_schema(description="Retrieve list of user profiles"),
    retrieve=extend_schema(description="Retrieve a single user profile"),
    create=extend_schema(description="Create a new user profile"),
    update=extend_schema(description="Update a user profile"),
    partial_update=extend_schema(description="Partially update a user profile"),
    destroy=extend_schema(description="Delete a user profile")
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