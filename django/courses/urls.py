from django.urls import path
from courses.views import CourseHomeView, CourseStudy
from courses.views import CourseDetail, SectorCourse, SearchCourse, AddComment, GetCartDetails

urlpatterns = [
    path('', CourseHomeView.as_view()),
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('<uuid:sector_uuid>/', SectorCourse.as_view()),
    path('search/<str:search_term>/', SearchCourse.as_view()),
    path('comment/<course_uuid>/', AddComment.as_view()),
    path('cart/', GetCartDetails.as_view()),
    path('study/<uuid:course_uuid>/', CourseStudy.as_view()),

]
