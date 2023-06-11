from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from .models import Sector, Course
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseDisplaySerializer, CourseUnpaidSerializer

class CourseHomeView(APIView):

    def get(self, request, *args, **kwargs):
        sectors = Sector.objects.order_by('?')[:6]

        sector_response = []

        for sector in sectors:
            sector_courses = sector.related_course.order_by('?')[:4]
            course_Serializer = CourseDisplaySerializer(sector_courses, many=True)

            sector_obj = {
                'sector_name':sector.name,
                'sector_uuid':sector.sector_uuid,
                'featured_course':course_Serializer.data,
                'selecor_image':sector.get_image_absolute_url()
            }

            sector_response.append(sector_obj)
        return Response(data=sector_response,status=status.HTTP_200_OK)


class CourseDetail(APIView):
    def get(self, request, course_uuid, *args, **kwargs):
        course = Course.objects.filter(course_uuid=course_uuid)
        if not course:
            return HttpResponseBadRequest('Course does not exist')
        
        serializer = CourseUnpaidSerializer(course[0])

        return Response(data = serializer.data, status = status.HTTP_200_OK)
