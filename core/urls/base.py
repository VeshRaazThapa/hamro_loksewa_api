from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import include, path
from rest_framework import routers
from apps.user.views import UserProfileViewSet,UserRoleViewSet,AreasOfPreparationsViewSet,UserFieldOfInterestsViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from ..views import auth as auth_views
from .auth import auth_urlpatterns
from django.urls import path
from apps.package.urls import package_urlpatterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users-profile', UserProfileViewSet)
router.register(r'user-roles',UserRoleViewSet)
router.register(r'areas-of-preparation',AreasOfPreparationsViewSet)
router.register(r'user-field-of-interests',UserFieldOfInterestsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),  # Admin URL
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
# login URLs for the browsable API.
urlpatterns += auth_urlpatterns
urlpatterns += package_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
