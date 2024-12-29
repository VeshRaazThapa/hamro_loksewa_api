from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(UserProfile)
admin.site.register(AreasOfPreparations)
admin.site.register(UserFieldOfInterests)

