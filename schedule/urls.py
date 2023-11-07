from django.urls import path
from .views import CourseDetailView, CourseListView

urlpatterns = [
    path('schedule/main/', CourseListView.as_view(), name='courses'),
    path('schedule/course_details/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
]
