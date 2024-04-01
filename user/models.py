from django.db import models
from ckeditor.fields import RichTextField
from core.models import Location
from django.urls import reverse
# Create your models here.

USER_TYPE_CHOICES = (
    ('student', 'student'),
    ('instructor', 'instructor'),
    ('parent', 'parent')
)

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    account_type = models.CharField(choices=USER_TYPE_CHOICES, default='student', max_length=12)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='profiles')
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = RichTextField(null=True, blank=True)
    position = models.CharField(help_text='e.g Developer etc', max_length=60, null=True, blank=True)
    phone_number = models.CharField(help_text='use format +254...', max_length=13, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_instructor = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} profile"
    
    def get_absolute_url(self):
        if self.account_type == 'instructor':
            return reverse('instructor:detail', kwargs={'username':self.user.username})
        
    def get_total_students(self):
        if self.account_type == 'instructor':
            students = 0
            for course in self.user.courses.all():
                students += course.students.all().count()
            return students
        else:
            return 0
        
    def get_avg_rating(self):
        return 5.0

class SocialMedia(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='social')
    facebook = models.URLField(max_length=120, null=True, blank=True, unique=True)
    linkedin = models.URLField(max_length=120, null=True, blank=True, unique=True)
    instagram = models.URLField(max_length=120, null=True, blank=True, unique=True)
    twitter = models.URLField(max_length=120, null=True, blank=True, unique=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} social accounts"
