from django.contrib import admin
from .models import Category, Course, Lesson, Unit, Review, AcademicLevel
# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'owner', 'created_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['owner']
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_per_page = 50

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'academic_level', 'category', 'owner', 'level', 'is_active', 'has_certificate', 'price', 'updated_at', 'created_at']
    search_fields = ['title', 'slug', 'price', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['owner', 'category', 'academic_level', 'students']
    list_filter = ['academic_level', 'level', 'is_active', 'has_certificate', 'created_at', 'updated_at']
    list_per_page = 50
    inlines = [ReviewInline,]

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'is_active', 'created_at']
    search_fields = ['title', 'overview']
    autocomplete_fields = ['course']
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_per_page = 50
    ordering = ('order', )
    inlines = [LessonInline,]

@admin.register(AcademicLevel)
class AcademicLevelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    list_per_page = 50