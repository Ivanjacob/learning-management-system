from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name="enrolled_courses")


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateField()


class Chat(models.Model):
    sender = models.ForeignKey(User, related_name="sent_message", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} on {self.timestamp}"
    

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.FloatField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"Grade {self.grade} for {self.student.username} in {self.assignment.title}"


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    topic = models.CharField(max_length=255)

