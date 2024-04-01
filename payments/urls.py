from django.urls import path

from . import views

app_name = 'payments'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('<slug:slug>/checkout-session/', views.create_checkout_session, name='session'),
    path('<slug:slug>/success/', views.SuccessView.as_view()),
    path('<slug:slug>/cancelled/', views.CancelledView.as_view()),
]