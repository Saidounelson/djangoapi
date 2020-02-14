"""

"""

from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @action(detail=False, methods=['post'], url_path='create')
    def create_courses(self, request):
        data = request.data
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["get"], url_path='list-course')
    def list_course(self, request):
        queryset = Course.objects.all()
        #serializer_class = CourseSerializer
        return Response(queryset)
    
    

    
