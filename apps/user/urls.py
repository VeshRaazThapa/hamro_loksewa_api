from django.contrib.auth.decorators import login_required
from .views import ForgotPasswordInitiateView, ResetPasswordView
from django.urls import path

from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('password/forgot/', ForgotPasswordInitiateView.as_view(), name='forgot-password'),
    path('password/reset/', ResetPasswordView.as_view(), name='reset-password'),
]
