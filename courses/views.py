from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the currently authenticated user to the course
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Ensure users only see their own courses
        return Course.objects.filter(user=self.request.user)
