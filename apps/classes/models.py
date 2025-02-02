import os
from django.conf import settings
from django.db import models
from apps.package.models import Package, AreasOfPreparations
from django.utils.translation import gettext_lazy as _

class Classes(models.Model):
    TYPE_CHOICES = (
        ('live', 'Live'),
        ('recorded', 'Recorded'),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    meeting_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    schedule = models.DateTimeField(null=True, blank=True)
    # package = models.ForeignKey(Package, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        class_videos = ClassVideos.objects.filter(class_id=self.id)
        if self.meeting_url and class_videos.exists():
            raise ValidationError('Only one of meeting_url or video_url should be provided.')
        if not self.meeting_url and not class_videos.exists():
            raise ValidationError('At least one of meeting_url or video_url must be provided.')

    def save(self, *args, **kwargs):
        self.updated_at = models.DateTimeField(auto_now=True)
        super().save(*args, **kwargs)

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    profile_image_url = models.ImageField(upload_to='instructor/profile/')
    teaching_area = models.ForeignKey(AreasOfPreparations, on_delete=models.CASCADE)
    years_of_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = models.DateTimeField(auto_now=True)
        super().save(*args, **kwargs)

class ClassInstructors(models.Model):
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = models.DateTimeField(auto_now=True)
        super().save(*args, **kwargs)

class ClassVideos(models.Model):
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    chapter = models.IntegerField(null=True, blank=True)
    thumbnail_url = models.CharField(max_length=255, null=True, blank=True)
    video_url = models.CharField(max_length=255)
    video_length_in_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = models.DateTimeField(auto_now=True)
        super().save(*args, **kwargs)
