from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from apps.user.models import PhoneDirectory

class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            # Find the user by phone number
            phone_directory = PhoneDirectory.objects.get(phone=phone, is_verified=True)
            user_profile = phone_directory.users.first()  # Get the UserProfile associated with the phone
            
            if user_profile:
                # Check if password matches
                user = user_profile.user
                if user.check_password(password):
                    return user
        except PhoneDirectory.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
