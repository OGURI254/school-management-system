from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('courses/', include('course.urls')),
    path('accounts/', include('allauth.urls')),
    path('students/', include('student.urls')),
    path('instructors/', include('instructor.urls')),
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Educonnect Admin'
admin.site.site_title = 'Educonnect Admin'
