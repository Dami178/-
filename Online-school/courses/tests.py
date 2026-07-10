from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Webinar, Homework, HomeworkSubmission

User = get_user_model()

class CoursesTestCase(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='password', role='teacher')
        self.student = User.objects.create_user(username='student', password='password', role='student')
        self.curator = User.objects.create_user(username='curator', password='password', role='curator')

        self.webinar = Webinar.objects.create(title='Math 101', video_url='http://example.com/math101', teacher=self.teacher)
        self.homework = Homework.objects.create(title='Math Homework 1', description='Solve 2+2', webinar=self.webinar)

    def test_models_creation(self):
        self.assertEqual(Webinar.objects.count(), 1)
        self.assertEqual(Homework.objects.count(), 1)

    def test_student_submission(self):
        self.client.login(username='student', password='password')
        response = self.client.post(f'/homework/{self.homework.id}/', {'answer': '4'})
        self.assertEqual(response.status_code, 302) # redirect after success
        self.assertEqual(HomeworkSubmission.objects.count(), 1)

        submission = HomeworkSubmission.objects.first()
        self.assertEqual(submission.answer, '4')
        self.assertEqual(submission.status, 'pending')

    def test_curator_grading(self):
        submission = HomeworkSubmission.objects.create(homework=self.homework, student=self.student, answer='4')
        self.client.login(username='curator', password='password')
        response = self.client.post(f'/curation/review/{submission.id}/', {'grade': '100', 'comment': 'Good job!'})
        self.assertEqual(response.status_code, 302) # redirect after grading

        submission.refresh_from_db()
        self.assertEqual(submission.grade, 100)
        self.assertEqual(submission.curator_comment, 'Good job!')
        self.assertEqual(submission.status, 'graded')
        self.assertEqual(submission.curator, self.curator)

    def test_webinar_list_view(self):
        response = self.client.get(reverse('courses:webinar_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/webinar_list.html')
        self.assertContains(response, 'Math 101')
