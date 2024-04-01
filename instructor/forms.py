from django import forms
from user.models import Profile, SocialMedia
from django.contrib.auth.models import User
from course.models import Course
from .models import Apply

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['image','location','phone_number','date_of_birth','position','bio']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['facebook', 'linkedin', 'instagram', 'twitter']


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'academic_level', 'front_image', 'cover_image', 'category', 'level', 'overview', 'price', 'preview_video', 'has_certificate']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        exclude = ('user','is_approved')

