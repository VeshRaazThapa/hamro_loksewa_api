from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db import models
from apps.user.models import AreasOfPreparations
from django.utils.text import slugify
import uuid
class Province(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

# kendra or sangha
class Association(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

# Examples: 'Physics', 'Chemistry'
class PackageCategory(models.Model):
    name = models.CharField(max_length=255, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Examples: 'Primary', 'Secondary'
class PackageSubCategory(models.Model):
    name = models.CharField(max_length=255, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    title = models.CharField(max_length=255, null=False)
    areas_of_preparation = models.ForeignKey(
            AreasOfPreparations,
            related_name="packages",
            on_delete=models.CASCADE
    )    
    category = models.ForeignKey(PackageCategory, on_delete=models.CASCADE, related_name='packages')
    sub_category = models.ForeignKey(PackageSubCategory, on_delete=models.CASCADE, related_name='packages')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_in_months = models.IntegerField(null=False)
    features = models.JSONField(null=False)  # Requires Django 3.1+
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True, related_name='packages')
    association = models.ForeignKey(Association, on_delete=models.SET_NULL, null=True, blank=True, related_name='packages')
    slug=models.SlugField(null=True, blank=True,unique=True)
    seo_title = models.CharField(max_length=500, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    seo_twitter_card_type = models.CharField(max_length=500, null=True, blank=True)
    seo_card_image = models.FileField(upload_to='package/seo/', null=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from the name, appending a UUID if necessary to ensure uniqueness
            base_slug = slugify(self.title) if self.title else str(uuid.uuid4())
            slug = base_slug
            counter = 1
            while Package.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class UserPackage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="packages", on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='user_packages')
    payment_id = models.IntegerField()  # Replace with ForeignKey if related table exists
    expiry_at = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user_id} - Package {self.package.title}"

class Subscription(models.Model):
    BASIC = 'basic'
    ADVANCED = 'advanced'
    PREMIUM = 'premium'

    SUBSCRIPTION_CHOICES = [
        (BASIC, 'Basic'),
        (ADVANCED, 'Advanced'),
        (PREMIUM, 'Premium'),
    ]

    name = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_in_months = models.IntegerField(null=False)
    features = models.JSONField(null=False)  # Requires Django 3.1+
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name.capitalize()} Subscription"


class UserSubscription(models.Model):
    ACTIVE = 'active'
    CANCELLED = 'cancelled'
    EXPIRED = 'expired'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (EXPIRED, 'Expired'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="subscriptions", on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='user_subscriptions')
    payment_id = models.IntegerField()  # Replace with ForeignKey if related table exists
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    expiry_at = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user_id} - {self.subscription_type.name.capitalize()} Subscription"


class Payment(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    ESEWA = 'esewa'
    KHALTI = 'khalti'

    METHOD_CHOICES = [
        (ESEWA, 'eSewa'),
        (KHALTI, 'Khalti'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="payments", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    package_id = models.IntegerField(null=True, blank=True)  # Add ForeignKey if related table exists
    subscription_id = models.IntegerField(null=True, blank=True)  # Add ForeignKey if related table exists

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(models.Q(package_id__isnull=False) | models.Q(subscription_id__isnull=False)) &
                      ~(models.Q(package_id__isnull=False) & models.Q(subscription_id__isnull=False)),
                name='check_package_or_subscription'
            )
        ]

    def __str__(self):
        return f"Payment {self.id} - Status: {self.status.capitalize()}"


class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured_image = models.ImageField(upload_to='ebooks/images/')
    file_url = models.FileField(upload_to='ebooks/files/')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ebooks'
        ordering = ['-created_at']
        verbose_name = 'Ebook'
        verbose_name_plural = 'Ebooks'

    def __str__(self):
        return self.title
