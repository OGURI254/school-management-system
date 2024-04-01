from django.contrib import admin
from .models import Tag, Blog, Review, Contact, Location
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    list_per_page = 50

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_published', 'published_at', 'created_at', 'updated_at']
    autocomplete_fields = ['author', 'category', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'category__title', 'description']
    list_filter = ['category', 'is_published', 'published_at', 'created_at']
    list_per_page = 50

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'ratings', 'user', 'is_active', 'created_at', 'updated_at']
    autocomplete_fields = ['user',]
    search_fields = ['ratings', 'message']
    list_filter = ['updated_at', 'created_at']
    list_per_page = 50

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'is_addressed', 'created_at', 'updated_at']
    search_fields = ['subject', 'name', 'email', 'message']
    list_filter = ['is_addressed', 'updated_at', 'created_at']
    list_per_page = 50

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'updated_at', 'created_at']
    list_per_page = 50