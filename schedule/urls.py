from django.urls import path
from .views import CourseListView, CourseDetailView, TeacherDetailView

urlpatterns = [
    path('schedule/main/', CourseListView.as_view(), name='courses'),
    path('schedule/course_details/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('schedule/teacher_details/<int:pk>', TeacherDetailView.as_view(), name='teacher-detail'),
]
