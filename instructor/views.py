from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.contrib import messages
from core.models import Location
from instructor.forms import ApplicationForm
from user.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import AddCourseForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from core.decorators import require_superuser_or_instructor
from course.models import Review
import uuid

# Create your views here.
@login_required
@require_superuser_or_instructor
def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'instructor/dashboard.html', context)

@login_required
@require_superuser_or_instructor
def list(request):
    query = request.GET.get('q', None)
    location = request.GET.get('location', None)
    order_by_filter = request.GET.get('f', None)

    instructors = Profile.objects.filter(account_type='instructor', user__is_active=True)

    if query:
        instructors = instructors.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query))

    if location:
        instructors = instructors.filter(location__title=location)

    if order_by_filter:
        if order_by_filter == 'recent':
            instructors = instructors.order_by('-updated_at')
        elif order_by_filter == 'courses':
            instructors = instructors.annotate(num_courses=Count('user__courses')).order_by('-num_courses')
        elif order_by_filter == 'near':                         
            if request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.location:
                instructors = instructors.filter(location=request.user.profile.location)
            else:
                messages.warning(request, f'Complete your profile to get instructors around you')

    paginator = Paginator(instructors, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'title': 'Instructors List',
        'locations': Location.objects.filter(is_active=True),
        'instructors': page_obj
    }

    return render(request, 'instructor/list.html', context)

@login_required
@require_superuser_or_instructor
def details(request, username):
    instructor = get_object_or_404(Profile, user__username=username, user__is_active=True)
    courses = instructor.user.courses.filter(is_active=True)
    query = request.GET.get('q', None)
    if query:
        courses = courses.filter(Q(title__icontains=query))

    paginator = Paginator(courses, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        'title': instructor.user.get_full_name(),
        'instructor': instructor,
        'courses': page_obj
    }
    return render(request, 'instructor/details.html', context)

@login_required
@require_superuser_or_instructor
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            try:
                application =  form.save(commit=False)
                application.user=request.user
                application.save()
                messages.success(request, "Applied Successfully!")
                return redirect('core:dashboard')
            except Exception as e:
                messages.warning(request, f"{e}")
                return redirect('instructor:apply')
    else:
        form = ApplicationForm()
    
    context = {
        'title': 'Apply to Become tutor',
        'form': form
    }
    return render(request, 'instructor/apply.html', context)

@login_required
@require_superuser_or_instructor
def courses(request):

    context = {
        'title': 'My Courses',
    }
    return render(request, 'instructor/courses.html', context)

@login_required
@require_superuser_or_instructor
def reviews(request):

    context = {
        'title': 'My Reviews',
        'reviews': Review.objects.filter(course__owner=request.user)
    }
    return render(request, 'instructor/reviews.html', context)

@login_required
@require_superuser_or_instructor
def students(request):

    context = {
        'title': 'My Students',
    }
    return render(request, 'instructor/students.html', context)

@login_required
@require_superuser_or_instructor
def add_course(request):
    user_instance = request.user

    if request.method == 'POST':
        add_course_form = AddCourseForm(request.POST, request.FILES)
        if add_course_form.is_valid():
            course = add_course_form.save(commit=False)
            course.owner = user_instance
            course.slug = slugify(course.title) + '-' + str(uuid.uuid4())[:8]
            course.save()
            messages.success(request, 'Courses Successfully Added!')
            return redirect('instructor:detail', user_instance.username)
    else:
        add_course_form = AddCourseForm()

    context = {
        'title': 'Add Course',
        'add_course_form': add_course_form,
    }
    return render(request, 'instructor/add_course.html', context)
