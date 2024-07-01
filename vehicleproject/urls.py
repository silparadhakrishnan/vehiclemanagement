"""
URL configuration for vehicleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="home_view"),
    path('userhome',views.UserHome.as_view(),name="user_home"),
    path('reg',views.UserRegisterView.as_view(),name="reg_view"),
    path('log',views.UserLoginView.as_view(),name="log_view"),
    path('logout',views.UserlogoutView.as_view(),name="logout_view"),
    path('pro',views.UserProfileView.as_view(),name="user_pro")
    
]
