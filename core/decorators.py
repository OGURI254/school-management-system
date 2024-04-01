from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from course.models import Course

def require_superuser_or_instructor(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser or request.user.profile.is_instructor:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to access this page!")
            return redirect('core:index')
    return _wrapped_view

def require_superuser_or_student(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser or not request.user.profile.is_instructor:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to access this page!")
            return redirect('core:index')
    return _wrapped_view

def require_enrollement(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        slug = kwargs.get('slug')
        course = Course.objects.filter(slug=slug).first()
        if request.user.is_authenticated and course and request.user in course.students.all():
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to access this page or not enrolled in this course!")
            return redirect('course:overview', slug)
    return _wrapped_view