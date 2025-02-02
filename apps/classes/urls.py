from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', ClassesViewSet)
router.register(r'instructor', InstructorViewSet)
router.register(r'classinstructors', ClassInstructorsViewSet)
router.register(r'classvideos', ClassVideosViewSet)

class_urlpatterns = [
    path('', include(router.urls)),
]

