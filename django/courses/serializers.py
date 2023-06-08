from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Course

class CourseDisplaySerializer(ModelSerializer):
    student_no = serializers.IntegerField(source = 'get_enrolled_student')
    author = UserSerializer()
    image_url = serializers.CharField(source = 'get_absolute_image_url')
    class Meta:
        model = Course
        fields = [
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url'
        ]