from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Comment, Course, Episode, CourseSection

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

class CommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        exclude = ['id']


class EpisodeUnpaidSerializer(ModelSerializer):
    lenght = serializers.CharField(source = 'get_video_length_time')
    class Meta:
        model = Episode
        fields = ['file']

class CourseSectionPaidSerializer(ModelSerializer):
    episodes = EpisodeUnpaidSerializer(many=True)
    total_duration = serializers.CharField(source='total_lenght')
    class Meta:
        fields = ['section_title','episodes','total_duration']


class EpisodeUnPaidSerializer(ModelSerializer):
    length = serializers.CharField(source='get_video_length_time')
    class Meta:
        model = Episode
        exclude = ['file']


class CourseSectionUnpaidSerializer(ModelSerializer):
    episodes = EpisodeUnPaidSerializer(many=True)
    total_duration = serializers.CharField(source = 'total_lenght')
    class Meta:
        model = CourseSection
        fields = ['section_title', 'episodes', 'total_duration',]

class CourseUnpaidSerializer(ModelSerializer):

    comments = CommentSerializer(many=True)
    author = UserSerializer()
    course_section = CourseSectionPaidSerializer(many=True)
    student_no = serializers.IntegerField(source='get_enrolled_student')
    total_lectures = serializers.IntegerField(source='get_total_lectures')
    total_duration = serializers.CharField(source='total_course_length')
    class Meta:
        model = Course
        exclude =['id']

