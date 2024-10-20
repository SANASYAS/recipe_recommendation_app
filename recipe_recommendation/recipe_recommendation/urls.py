
from django.contrib import admin
from django.urls import path,include
from recipes import views  # Import the views from the recipes app

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('recipes.urls')),  # Include URLs from the recipes app
    path('', views.home, name='home'),  # Add this line for the home page
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('recipes/', include('recipes.urls')),  # Include the URLs from the recipes app
    
]
