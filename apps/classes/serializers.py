from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Classes, Instructor, ClassInstructors, ClassVideos
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class ClassInstructorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInstructors
        fields = '__all__'

class ClassVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassVideos
        fields = '__all__'