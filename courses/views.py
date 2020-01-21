from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @action(detail=False, methods=['post'])
    def create_courses(self, request):
        data = request.data
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["post"])
    def update_course(self, request):
        
        pass
    
class AutresViews(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @action(detail=True, methods=['post'])
    def test(self, request,pk=None):
        print("test")
        pass
    

    
