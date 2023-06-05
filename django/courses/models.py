import uuid
from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=255)
    sector_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    related_course = models.ManyToManyField('Course')
    sector_image = models.ImageField(upload_to='sector_image')

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User)
    language = models.CharField(max_length=50)
    course_section = models.ManyToManyField('CourseSection')
    comments = models.ManyToManyField('Comment')
    image_url = models.ImageField(upload_to='course_images')
    course_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    price =  models.DecimalField(max_digits=5, decimal_places=2)
#Course

class CourseSection(models.Model):
    title = models.CharField(max_length=255)
    episodes = models.ManyToManyField('Episode')
#Course Section
class Episode(models.Model):
    title = models.CharField(max_length=255)
    file=models.FileField(upload_to='course_video')
    length=models.DateTimeField(max_length=10, decimal_places=2)
#Episode

class Comment(models.Model):
    # user = models.ForeignKey(User)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)