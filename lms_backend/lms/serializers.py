
from rest_framework import serializers

from .models import Course, Assignment, Schedule, Chat, Grade


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Chat
        fields = [
            'id',
            'sender',
            'receiver',
            'message',
            'timestamp',
            'course'
        ]


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.username')
    assignment = serializers.ReadOnlyField(source='assignment.title')

    class Meta:
        model = Grade
        fields = [
            'id',
            'student',
            'assignment',
            'grade',
            'feedback'
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = Schedule
        fields = [
            'id',
            'course',
            'date',
            'start_time',
            'end_time',
            'topic'
        ]
