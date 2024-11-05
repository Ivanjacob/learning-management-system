from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, AssignmentViewSet, ChatViewSet, GradeViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'schedule', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('api/', include(router.urls)),
]
