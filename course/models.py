from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import striptags, escape
# Create your models here.
class AcademicLevel(models.Model):
    title = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course:list_by_academic', kwargs={'a_slug': self.slug})
    
    class Meta:
        ordering = ('created_at',)

class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course:list_by_categories', kwargs={'slug': self.slug})
    
    def get_blogs_url(self):
        return reverse('core:blog_list_by_category', kwargs={'c_slug': self.slug})

    class Meta:
        ordering = ('title',)

class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('expert', 'expert')
    )
    title = models.CharField(max_length=120)
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, related_name='courses')
    slug = models.SlugField(max_length=200, unique=True)
    front_image = models.ImageField(upload_to='courses/front/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='courses/cover/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='courses')
    level = models.CharField(choices=LEVEL_CHOICES, default='beginner', max_length=20)
    students = models.ManyToManyField('auth.User', blank=True, related_name='enrolled_courses')
    overview = RichTextField()
    is_active = models.BooleanField(default=True)
    has_certificate = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    preview_video = models.URLField(max_length=300, help_text='can be video from youtube')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course:overview', kwargs={'slug': self.slug})
    
    def get_payment_url(self):
        return reverse('payments:session', kwargs={'slug': self.slug})
    
    def get_overview(self):
        cleaned_description = striptags(self.overview)[:200]
        cleaned_description = escape(cleaned_description)
        return cleaned_description
    
    def get_avg_rating(self):
        avg_rating = self.reviews.aggregate(models.Avg('ratings'))['ratings__avg']
        if avg_rating is not None:
            return round(avg_rating, 1)
        else:
            return None
    
    class Meta:
        ordering = ('-created_at',)

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units')
    order = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=120)
    overview = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('order',)

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='lessons')
    order = models.PositiveSmallIntegerField()
    document = models.FileField(upload_to='category/courses/documents/', null=True, blank=True)
    video = models.URLField(null=True, blank=True, help_text='videos has to be from youtube')
    notes = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lecture {self.unit.order}.{self.order}: {self.title}"
    
    def get_absolute_url(self):
        return reverse('course:details', kwargs={'slug': self.unit.course.slug, 'id':self.id})
    
    class Meta:
        ordering = ('order',)

RATING_CHOICES = (
    (1,1),(2,2),(3,3),(4,4),(5,5)
)

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='left_reviews')
    ratings = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    message = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
        
    class Meta:
        ordering = ('-created_at',)