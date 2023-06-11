from django.urls import path
from courses.views import CourseHomeView
from courses.views import CourseDetail

urlpatterns = [
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('', CourseHomeView.as_view())
]
