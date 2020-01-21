from rest_framework import routers, serializers, viewsets
from .models import Course
from rest_framework import routers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name','language','price')