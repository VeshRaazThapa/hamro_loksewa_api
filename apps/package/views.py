from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Province, Association, PackageCategory, PackageSubCategory,
    Package, UserPackage, Subscription, UserSubscription, Payment,Ebook
)
from .serializers import (
    ProvinceSerializer, AssociationSerializer, PackageCategorySerializer,
    PackageSubCategorySerializer, PackageSerializer, UserPackageSerializer,
    SubscriptionSerializer, UserSubscriptionSerializer, PaymentSerializer,EbookSerializer
)
from rest_framework.decorators import permission_classes

@extend_schema_view(
    list=extend_schema(summary="List all provinces", description="Retrieve a list of all provinces."),
    retrieve=extend_schema(summary="Retrieve a province", description="Retrieve a single province by ID."),
    create=extend_schema(summary="Create a new province", description="Create a new province entry."),
    update=extend_schema(summary="Update a province", description="Update an existing province."),
    partial_update=extend_schema(summary="Partially update a province", description="Partially update a province entry."),
    destroy=extend_schema(summary="Delete a province", description="Delete a province entry."),
)
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def get_permissions(self):
        # Allow unauthenticated access to the `list` action
        if self.action == 'list':
            return [AllowAny()]
        # Require authentication for all other actions
        return [IsAuthenticated()]
@extend_schema_view(
    list=extend_schema(summary="List all associations", description="Retrieve a list of all associations."),
    retrieve=extend_schema(summary="Retrieve an association", description="Retrieve a single association by ID."),
    create=extend_schema(summary="Create a new association", description="Create a new association entry."),
    update=extend_schema(summary="Update an association", description="Update an existing association."),
    partial_update=extend_schema(summary="Partially update an association", description="Partially update an association entry."),
    destroy=extend_schema(summary="Delete an association", description="Delete an association entry."),
)
class AssociationViewSet(viewsets.ModelViewSet):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
        
    def get_permissions(self):
        # Allow unauthenticated access to the `list` action
        if self.action == 'list':
            return [AllowAny()]
        # Require authentication for all other actions
        return [IsAuthenticated()]
    
@extend_schema_view(
    list=extend_schema(summary="List all package categories", description="Retrieve a list of all package categories."),
    retrieve=extend_schema(summary="Retrieve a package category", description="Retrieve a single package category by ID."),
    create=extend_schema(summary="Create a new package category", description="Create a new package category entry."),
    update=extend_schema(summary="Update a package category", description="Update an existing package category."),
    partial_update=extend_schema(summary="Partially update a package category", description="Partially update a package category entry."),
    destroy=extend_schema(summary="Delete a package category", description="Delete a package category entry."),
)
class PackageCategoryViewSet(viewsets.ModelViewSet):
    queryset = PackageCategory.objects.all()
    serializer_class = PackageCategorySerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all package subcategories", description="Retrieve a list of all package subcategories."),
    retrieve=extend_schema(summary="Retrieve a package subcategory", description="Retrieve a single package subcategory by ID."),
    create=extend_schema(summary="Create a new package subcategory", description="Create a new package subcategory entry."),
    update=extend_schema(summary="Update a package subcategory", description="Update an existing package subcategory."),
    partial_update=extend_schema(summary="Partially update a package subcategory", description="Partially update a package subcategory entry."),
    destroy=extend_schema(summary="Delete a package subcategory", description="Delete a package subcategory entry."),
)
class PackageSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = PackageSubCategory.objects.all()
    serializer_class = PackageSubCategorySerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all packages", description="Retrieve a list of all packages."),
    retrieve=extend_schema(summary="Retrieve a package", description="Retrieve a single package by ID."),
    create=extend_schema(summary="Create a new package", description="Create a new package entry."),
    update=extend_schema(summary="Update a package", description="Update an existing package."),
    partial_update=extend_schema(summary="Partially update a package", description="Partially update a package entry."),
    destroy=extend_schema(summary="Delete a package", description="Delete a package entry."),
)
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all user packages", description="Retrieve a list of all user packages."),
    retrieve=extend_schema(summary="Retrieve a user package", description="Retrieve a single user package by ID."),
    create=extend_schema(summary="Create a new user package", description="Create a new user package entry."),
    update=extend_schema(summary="Update a user package", description="Update an existing user package."),
    partial_update=extend_schema(summary="Partially update a user package", description="Partially update a user package entry."),
    destroy=extend_schema(summary="Delete a user package", description="Delete a user package entry."),
)
class UserPackageViewSet(viewsets.ModelViewSet):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all subscriptions", description="Retrieve a list of all subscriptions."),
    retrieve=extend_schema(summary="Retrieve a subscription", description="Retrieve a single subscription by ID."),
    create=extend_schema(summary="Create a new subscription", description="Create a new subscription entry."),
    update=extend_schema(summary="Update a subscription", description="Update an existing subscription."),
    partial_update=extend_schema(summary="Partially update a subscription", description="Partially update a subscription entry."),
    destroy=extend_schema(summary="Delete a subscription", description="Delete a subscription entry."),
)
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all user subscriptions", description="Retrieve a list of all user subscriptions."),
    retrieve=extend_schema(summary="Retrieve a user subscription", description="Retrieve a single user subscription by ID."),
    create=extend_schema(summary="Create a new user subscription", description="Create a new user subscription entry."),
    update=extend_schema(summary="Update a user subscription", description="Update an existing user subscription."),
    partial_update=extend_schema(summary="Partially update a user subscription", description="Partially update a user subscription entry."),
    destroy=extend_schema(summary="Delete a user subscription", description="Delete a user subscription entry."),
)
class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all payments", description="Retrieve a list of all payments."),
    retrieve=extend_schema(summary="Retrieve a payment", description="Retrieve a single payment by ID."),
    create=extend_schema(summary="Create a new payment", description="Create a new payment entry."),
    update=extend_schema(summary="Update a payment", description="Update an existing payment."),
    partial_update=extend_schema(summary="Partially update a payment", description="Partially update a payment entry."),
    destroy=extend_schema(summary="Delete a payment", description="Delete a payment entry."),
)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(summary="List all ebooks", description="Retrieve a list of all ebooks."),
    retrieve=extend_schema(summary="Retrieve a ebook", description="Retrieve a single ebook by ID."),
    create=extend_schema(summary="Create a new ebook", description="Create a new ebook entry."),
    update=extend_schema(summary="Update a ebook", description="Update an existing ebook."),
    partial_update=extend_schema(summary="Partially update a ebook", description="Partially update a payment entry."),
    destroy=extend_schema(summary="Delete a ebook", description="Delete a ebook entry."),
)
class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['package']
    search_fields = ['title', 'author', 'description']
    ordering_fields = ['created_at', 'updated_at']

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]