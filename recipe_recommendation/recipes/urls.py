from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('submit/', views.submit_contact, name='submit_contact'),
]


