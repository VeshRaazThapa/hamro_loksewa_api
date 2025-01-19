from django.urls import path, re_path
from django.contrib.auth import views as auth

from ..views import auth as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.user.views import SendOTPView, VerifyOTPView,CustomTokenObtainPairView

auth_urlpatterns = [
    # JWT Authentication
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("auth/send-otp/", SendOTPView.as_view(), name="send_otp"),
    path("auth/verify-otp/", VerifyOTPView.as_view(), name="verify_otp"),
    #  path('register', auth_views.register, name="register"),

    # Logout
    path('auth/logout/', auth_views.logout_view, name="Auth"),
    
]
