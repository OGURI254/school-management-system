from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faq, name='faq'),
    path('blogs/', views.blog, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blogs/categories/<slug:c_slug>/', views.blog, name='blog_list_by_category'),
    path('blogs/tags/<slug:t_slug>/', views.blog, name='blog_list_by_tag'),
    path('dashboard/', views.dashboard, name='dashboard'),
]