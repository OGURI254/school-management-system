from . import views
from django.urls import path, include

app_name = 'instructor'
urlpatterns = [
    path('', views.list, name='list'),
    path('apply/', views.apply, name='apply'),
    path('add_course/', views.add_course, name='add_course'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reviews/', views.reviews, name='reviews'),
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
    path('<str:username>/', views.details, name='detail'),
]
