from django.db import models

# Create your models here.
class Apply(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='application')
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    id_number = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)