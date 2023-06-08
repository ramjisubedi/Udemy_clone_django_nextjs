# Generated by Django 4.2.1 on 2023-06-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_section',
            field=models.ManyToManyField(blank=True, to='courses.coursesection'),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='episodes',
            field=models.ManyToManyField(blank=True, to='courses.episode'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='related_course',
            field=models.ManyToManyField(blank=True, to='courses.course'),
        ),
    ]