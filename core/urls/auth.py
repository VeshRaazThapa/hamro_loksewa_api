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
    


    # Password Reset
    # path('password-reset', auth_views.password_reset, name="password_reset"),
    # path('password-reset/<uidb64>/<token>/', auth_views.password_reset_confirm, name="password_reset_confirm"),
    # password reset
    # path('/auth/password-reset', auth.PasswordResetView.as_view(), name="password_reset"),
    # path('/auth/password-reset/done', auth.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('/auth/password-reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('/auth/reset/done', auth.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # change password
]
