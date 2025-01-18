from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Province, Association, PackageCategory, PackageSubCategory,
    Package, UserPackage, Subscription, UserSubscription, Payment
)
from .serializers import (
    ProvinceSerializer, AssociationSerializer, PackageCategorySerializer,
    PackageSubCategorySerializer, PackageSerializer, UserPackageSerializer,
    SubscriptionSerializer, UserSubscriptionSerializer, PaymentSerializer,
)

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [IsAuthenticated]

class AssociationViewSet(viewsets.ModelViewSet):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    permission_classes = [IsAuthenticated]

class PackageCategoryViewSet(viewsets.ModelViewSet):
    queryset = PackageCategory.objects.all()
    serializer_class = PackageCategorySerializer
    permission_classes = [IsAuthenticated]

class PackageSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = PackageSubCategory.objects.all()
    serializer_class = PackageSubCategorySerializer
    permission_classes = [IsAuthenticated]

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

class UserPackageViewSet(viewsets.ModelViewSet):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer
    permission_classes = [IsAuthenticated]

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]