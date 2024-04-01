from . import views
from django.urls import path, include

app_name = 'students'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reviews/', views.reviews, name='reviews'),
    path('courses/', views.courses, name='courses'),
    path('accounts/', views.accounts, name='accounts'),
    path('profile/', views.profile, name='profile'),
]
