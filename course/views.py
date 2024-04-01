from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Course, AcademicLevel, Lesson
from .forms import CourseReviewForm
from user.models import Profile
from django.contrib import messages
from django.core.paginator import Paginator
from core.decorators import require_enrollement
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request, slug=None, a_slug=None):
    category = None
    title = 'Courses'
    courses = Course.objects.filter(is_active=True)
    if slug:
        category = get_object_or_404(Category, slug=slug, is_active=True)
        title = f'Courses under {category.title}'
        courses = Course.objects.filter(is_active=True, category=category)
    elif a_slug:
        category = get_object_or_404(AcademicLevel, slug=a_slug)
        title = f'Courses under {category.title} Level'
        courses = Course.objects.filter(is_active=True, academic_level=category)

    paginator = Paginator(courses, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'title': title,
        'courses': page_obj,
        'categories': Category.objects.filter(is_active=True),
        'category': category,
        'academic_levels': AcademicLevel.objects.all(),
    }

    return render(request, 'course/index.html', context)

def course_overview(request, slug):
    course = get_object_or_404(Course, is_active=True, slug=slug)
    if request.user in course.students.all():
        return redirect('course:detail', slug)
    if request.method == 'POST':
        form = CourseReviewForm(request.POST)
        try:
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.course = course
                review.save()
                messages.success(request, f"Successfully left review for {course.title}")
                return redirect('course:overview', slug)
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('course:overview', slug)
    else:
        form = CourseReviewForm()
    context ={
        'title': course.title,
        'course': course,
        'form': form
    }
    return render(request, 'course/overview.html', context)

def categories(request):

    context = {
        'title': 'Categories',
        'categories': Category.objects.filter(is_active=True),
    }
    return render(request, 'course/categories.html', context)

@login_required
@require_enrollement
def course_detail(request, slug):
    course = get_object_or_404(Course, is_active=True, slug=slug)
    
    context ={
        'title': course.title,
        'course': course,
    }
    return render(request, 'course/details.html', context)

@login_required
@require_enrollement
def lesson_detail(request, slug, id):
    course = get_object_or_404(Course, is_active=True, slug=slug)
    lesson = get_object_or_404(Lesson, unit__course=course, is_active=True, id=id)

    context ={
        'title': course.title,
        'course': course,
        'lesson': lesson
    }
    return render(request, 'course/details.html', context)
