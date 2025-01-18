from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(UserProfile)
admin.site.register(AreasOfPreparations)
admin.site.register(UserFieldOfInterests)
admin.site.register(UserRole)
admin.site.register(Device)
admin.site.register(PhoneDirectory)

