from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Classes, Instructor, ClassInstructors,ClassVideos
from rest_framework import viewsets, permissions
from .serializers import ClassesSerializer,InstructorSerializer,ClassInstructorsSerializer, ClassVideosSerializer
# ViewSets with Permissions and DRF Spectacular
@extend_schema_view(
    list=extend_schema(summary="List all classes", description="Retrieve a list of all classes."),
    retrieve=extend_schema(summary="Retrieve a class", description="Retrieve a single class by ID."),
    create=extend_schema(summary="Create a new class", description="Create a new class entry."),
    update=extend_schema(summary="Update a class", description="Update an existing class."),
    partial_update=extend_schema(summary="Partially update a class", description="Partially update a class entry."),
    destroy=extend_schema(summary="Delete a class", description="Delete a class entry."),
)
class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

@extend_schema_view(
    list=extend_schema(summary="List all instructors", description="Retrieve a list of all instructors."),
    retrieve=extend_schema(summary="Retrieve an instructor", description="Retrieve a single instructor by ID."),
    create=extend_schema(summary="Create a new instructor", description="Create a new instructor entry."),
    update=extend_schema(summary="Update an instructor", description="Update an existing instructor."),
    partial_update=extend_schema(summary="Partially update an instructor", description="Partially update an instructor entry."),
    destroy=extend_schema(summary="Delete an instructor", description="Delete an instructor entry."),
)
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

@extend_schema_view(
    list=extend_schema(summary="List all class instructors", description="Retrieve a list of all class instructors."),
    retrieve=extend_schema(summary="Retrieve a class instructor", description="Retrieve a single class instructor by ID."),
    create=extend_schema(summary="Create a new class instructor", description="Create a new class instructor entry."),
    update=extend_schema(summary="Update a class instructor", description="Update an existing class instructor."),
    partial_update=extend_schema(summary="Partially update a class instructor", description="Partially update a class instructor entry."),
    destroy=extend_schema(summary="Delete a class instructor", description="Delete a class instructor entry."),
)
class ClassInstructorsViewSet(viewsets.ModelViewSet):
    queryset = ClassInstructors.objects.all()
    serializer_class = ClassInstructorsSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

@extend_schema_view(
    list=extend_schema(summary="List all class videos", description="Retrieve a list of all class videos."),
    retrieve=extend_schema(summary="Retrieve a class video", description="Retrieve a single class video by ID."),
    create=extend_schema(summary="Create a new class video", description="Create a new class video entry."),
    update=extend_schema(summary="Update a class video", description="Update an existing class video."),
    partial_update=extend_schema(summary="Partially update a class video", description="Partially update a class video entry."),
    destroy=extend_schema(summary="Delete a class video", description="Delete a class video entry."),
)
class ClassVideosViewSet(viewsets.ModelViewSet):
    queryset = ClassVideos.objects.all()
    serializer_class = ClassVideosSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]