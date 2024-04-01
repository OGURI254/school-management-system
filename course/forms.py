from django import forms
from .models import Review

class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('course', 'user', 'is_active')