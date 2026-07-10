from django.db import models
from django.conf import settings

class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='webinars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='homeworks')
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class HomeworkSubmission(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('graded', 'Graded'),
    )
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'student'}, related_name='submissions')
    answer = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    grade = models.IntegerField(null=True, blank=True)
    curator_comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    curator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'curator'}, related_name='graded_submissions')

    def __str__(self):
        return f"{self.student.username} - {self.homework.title}"
