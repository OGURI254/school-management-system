from django.contrib import admin
from .models import Profile, SocialMedia
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0

class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    can_delete = False
    extra = 0


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']
    ordering = ['date_joined',]
    list_filter = ['date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser']
    list_per_page = 20
    inlines = (ProfileInline, SocialMediaInline)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)