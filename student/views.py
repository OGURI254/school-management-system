from django.shortcuts import render
from course.models import Course
from django.contrib.auth.decorators import login_required
from core.decorators import require_superuser_or_student
# Create your views here.

@login_required
@require_superuser_or_student
def dashboard(request):
    context = {
        'title': "Dashboard",
        'courses': Course.objects.filter(is_active=True)
    }
    return render(request, 'student/dashboard.html', context)

@login_required
@require_superuser_or_student
def courses(request):
    courses = Course.objects.filter(students=request.user)
    context = {
        'title': "Enrolled Courses",
        'courses': courses
    }
    return render(request, 'student/courses.html', context)

@login_required
@require_superuser_or_student
def reviews(request):
    context = {
        'title': "Reviews Left"
    }
    return render(request, 'student/reviews.html', context)

@login_required
@require_superuser_or_student
def accounts(request):
    context = {
        'title': "Accounts Settings"
    }
    return render(request, 'student/accounts.html', context)

@login_required
@require_superuser_or_student
def profile(request):
    context = {
        'title': "User Profile"
    }
    return render(request, 'student/profile.html', context)

