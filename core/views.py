from django.shortcuts import render, get_object_or_404, redirect
from course.models import Category, Course
from user.models import Profile
from core.models import Review, Blog, Tag
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    instructors = Profile.objects.filter(account_type='instructor', user__is_active=True)
    if request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.location:
        instructors = instructors.filter(location=request.user.profile.location)
    else:
        messages.warning(request, f'Complete your profile to get instructors around you')
    context = {
        'title': 'Homepage',
        'categories': Category.objects.filter(is_active=True),
        'courses': Course.objects.filter(is_active=True)[:6],
        'tutors': Profile.objects.filter(account_type='instructure', user__is_active=True),
        'total_students': Profile.objects.filter(account_type='student').count(),
        'total_courses': Course.objects.all().count(),
        'total_users': Profile.objects.all().count(),
        'reviews': Review.objects.filter(is_active=True),
        'blogs': Blog.objects.filter(is_published=True),
        'instructors': instructors
    }
    return render(request, 'core/index.html', context)

def privacy(request):
    context = {
        'title': 'Privacy Policy'
    }
    return render(request, 'core/privacy.html', context)

def terms(request):
    context = {
        'title': 'Terms & Conditions'
    }
    return render(request, 'core/terms.html', context)

def search(request):
    query = request.GET.get('q')
    title = 'Search our databases'
    if query:
        title = f"20 results matched your query '{query}'"
        pass

    context = {
        'title': title
    }
    return render(request, 'core/search.html', context)

def blog(request, c_slug=None, t_slug=None):
    title = 'Blog posts'
    category = tag = None
    query = request.GET.get('q')
    blogs = Blog.objects.filter(is_published=True)
    if c_slug:
        category = get_object_or_404(Category, slug=c_slug)
        title = f'Blog posts under category {category.title}'
        blogs = blogs.filter(category=category)
    if t_slug:
        tag = get_object_or_404(Tag, slug=t_slug)
        title = f'Blog posts with tag {tag.title}'
        blogs = blogs.filter(tags=tag)
    if query:
        blogs = blogs.filter(title__icontains=query)

    context = {
        'title': title,
        'blogs': blogs,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'category': category
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, is_published=True, slug=slug)
    context = {
        'title': blog.title,
        'blog': blog,
        'blogs': Blog.objects.filter(is_published=True)[:5],
        'categories': Category.objects.all(),
        'tags': Tag.objects.all()
    }
    return render(request, 'blog/details.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your feedback has been submitted successfully!')
                return redirect('core:index')
        except Exception as e:
            messages.success(request, f'Error: {e}')
            return redirect('core:contact')
    else:
        form = ContactForm()
        
    context = {
        'title': 'Contact Us',
        'form': form
    }
    return render(request, 'core/contact.html', context)

def faq(request):
    context = {
        'title': 'Frequently Asked Questions'
    }
    return render(request, 'core/faq.html', context)

@login_required
def dashboard(request):
    if request.user.profile.is_instructor:
        return redirect('instructor:dashboard')
    else:
        return redirect('students:dashboard')

