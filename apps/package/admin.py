from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(Package)
admin.site.register(Province)
admin.site.register(PackageCategory)
admin.site.register(PackageSubCategory)
admin.site.register(Association)
admin.site.register(Subscription)
admin.site.register(UserPackage)
admin.site.register(UserSubscription)
admin.site.register(Payment)


