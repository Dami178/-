from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Webinar, Homework, HomeworkSubmission
from django.http import HttpResponseForbidden

def webinar_list(request):
    webinars = Webinar.objects.all().order_by('-created_at')
    return render(request, 'courses/webinar_list.html', {'webinars': webinars})

def webinar_detail(request, pk):
    webinar = get_object_or_404(Webinar, pk=pk)
    return render(request, 'courses/webinar_detail.html', {'webinar': webinar})

@login_required
def homework_detail(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    submission = None
    if request.user.role == 'student':
        submission = HomeworkSubmission.objects.filter(homework=homework, student=request.user).first()

    if request.method == 'POST' and request.user.role == 'student':
        answer = request.POST.get('answer')
        if not submission:
            submission = HomeworkSubmission(homework=homework, student=request.user, answer=answer)
        else:
            submission.answer = answer
        submission.save()
        return redirect('courses:homework_detail', pk=pk)

    return render(request, 'courses/homework_detail.html', {'homework': homework, 'submission': submission})

@login_required
def curation_list(request):
    if request.user.role != 'curator':
        return HttpResponseForbidden("Only curators can access this page.")
    submissions = HomeworkSubmission.objects.filter(status='pending').order_by('submitted_at')
    return render(request, 'courses/curation_list.html', {'submissions': submissions})

@login_required
def review_submission(request, pk):
    if request.user.role != 'curator':
        return HttpResponseForbidden("Only curators can access this page.")
    submission = get_object_or_404(HomeworkSubmission, pk=pk)
    if request.method == 'POST':
        grade = request.POST.get('grade')
        comment = request.POST.get('comment')
        submission.grade = grade
        submission.curator_comment = comment
        submission.status = 'graded'
        submission.curator = request.user
        submission.save()
        return redirect('courses:curation_list')
    return render(request, 'courses/review_submission.html', {'submission': submission})
