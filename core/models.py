from django.db import models
from django.urls import reverse
from course.models import Category
from ckeditor.fields import RichTextField
from django.template.defaultfilters import striptags, escape

class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_blogs_url(self):
        return reverse('core:blog_list_by_tag', kwargs={'t_slug': self.slug})
    
    class Meta:
        ordering = ('title',)

class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    cover_image = models.ImageField(upload_to='blogs/cover/', blank=True, null=True)
    front_image = models.ImageField(upload_to='blogs/front/', blank=True, null=True)
    description = RichTextField()
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:blog_detail', kwargs={'slug': self.slug})
    
    def get_overview(self):
        cleaned_description = striptags(self.description)[:200]
        cleaned_description = escape(cleaned_description)
        return cleaned_description
    
    class Meta:
        ordering = ('-published_at',)

RATING_CHOICES = (
    (1,1),(2,2),(3,3),(4,4),(5,5)
)
class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')
    ratings = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    message = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review left by {self.user.get_full_name()}"
    
    def get_overview(self):
        cleaned_description = striptags(self.message)[:200]
        cleaned_description = escape(cleaned_description)
        return cleaned_description
    
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=200)
    message = RichTextField()
    is_addressed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ('-created_at', 'is_addressed')

class Location(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)