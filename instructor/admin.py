from django.contrib import admin
from instructor.models import Apply
# Register your models here.

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'id_number', 'user', 'is_approved']
    list_filter = ['user', 'is_approved', 'created_at', 'updated_at']
    search_fields = ['name', 'email']
    date_hierarchy = 'created_at'
    actions = ['approve_instructor', 'cancel_instructor']

    def approve_instructor(self, request, queryset):
        queryset.update(is_approved=True)
        for apply_obj in queryset:
            apply_obj.user.profile.is_instructor = True
            apply_obj.user.profile.save()

    approve_instructor.short_description = "Approve selected instructors"

    def cancel_instructor(self, request, queryset):
        queryset.update(is_approved=False)
        for apply_obj in queryset:
            apply_obj.user.profile.is_instructor = False
            apply_obj.user.profile.save()

    cancel_instructor.short_description = "Cancel selected instructors"