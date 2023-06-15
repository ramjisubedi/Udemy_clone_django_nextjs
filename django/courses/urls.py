from django.urls import path
from courses.views import CourseHomeView
from courses.views import CourseDetail, SectorCourse

urlpatterns = [
    path('', CourseHomeView.as_view()),
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('<uuid:sector_uuid>/', SectorCourse.as_view())
]
