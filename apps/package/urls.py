from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProvinceViewSet, AssociationViewSet, PackageCategoryViewSet,
    PackageSubCategoryViewSet, PackageViewSet, UserPackageViewSet,
    SubscriptionViewSet, UserSubscriptionViewSet, PaymentViewSet,
)

router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'associations', AssociationViewSet)
router.register(r'package-categories', PackageCategoryViewSet)
router.register(r'package-subcategories', PackageSubCategoryViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'user-packages', UserPackageViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'user-subscriptions', UserSubscriptionViewSet)
router.register(r'payments', PaymentViewSet)

package_urlpatterns = [
    path('', include(router.urls)),
]
