from . import views
from django.urls import path, include

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.index, name='list_by_categories'),
    path('academic-levels/<slug:a_slug>/', views.index, name='list_by_academic'),
    path('<slug:slug>/', views.course_overview, name='overview'),
    path('<slug:slug>/details/', views.course_detail, name='detail'),
    path('<slug:slug>/details/<int:id>/', views.lesson_detail, name='details'),
]