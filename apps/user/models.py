import os
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import uuid
class PhoneDirectory(models.Model):
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.phone

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ("Male", _("Male")),
        ("Female", _("Female")),
        ("Other", _("Other"))
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, null=True, blank=True
    )
    phone_directory =  models.ForeignKey(
        PhoneDirectory,
        related_name="users",
        on_delete=models.SET_NULL,
        null=True,blank=True
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    experience_in_yrs = models.PositiveIntegerField(null=True, blank=True)
    profile_photo_url = models.ImageField(upload_to="user/profile/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class AreasOfPreparations(models.Model):
    name = models.CharField(max_length=255)
    # icon_name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='areas_of_prepration_icon/', null=True, blank=True, default=None)
    icon_svg = models.TextField(null=True, blank=True)
    slug=models.SlugField(null=True, blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from the name, appending a UUID if necessary to ensure uniqueness
            base_slug = slugify(self.name) if self.name else str(uuid.uuid4())
            slug = base_slug
            counter = 1
            while AreasOfPreparations.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class UserFieldOfInterests(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="field_of_interests",
        on_delete=models.CASCADE
    )
    areas_of_preparation = models.ForeignKey(
        AreasOfPreparations,
        related_name="areas_of_preparations",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'areas_of_preparation')  # Ensure no duplicate entries

    def __str__(self):
        return f"{self.user.username} - {self.areas_of_preparation.name}"
    
class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="roles", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="roles", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return u'User: {}\'s role: {}'.format(self.user.__str__(), self.group.__str__())

    @staticmethod
    def is_active(user, group):
        return UserRole.objects.filter(user=user, group__name=group, ended_at=None).exists()

class Device(models.Model):
    """
        Stores information about user devices for fcm notifications
    """
    device_id = models.CharField(max_length=100, null=True, blank=True)
    registration_id = models.TextField()
    email = models.CharField(max_length=100)