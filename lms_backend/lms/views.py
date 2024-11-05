from rest_framework import viewsets, permissions

from .models import Course, Assignment, Chat, Grade, Schedule
from .serializers import CourseSerializer, GradeSerializer, ScheduleSerializer, AssignmentSerializer, ChatSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('timestamp')
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow students to see their own grades
        if self.request.user.is_staff:
            return Grade.objects.all() # Admin/Teachers, show all grades 
        return Grade.objects.filter(student=self.request.user)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('date', 'start_time')
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow students to view the schedule of their enrolled courses
        return Schedule.objects.filter(course_students=self.request.user)


