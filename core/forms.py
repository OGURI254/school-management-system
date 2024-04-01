from .models import Contact
from django import forms
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('is_addressed', )
