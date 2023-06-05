from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User)
    language = models.CharField(max_length=50)


#Course
#Course Section
#Episode