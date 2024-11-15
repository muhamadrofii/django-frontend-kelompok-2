"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from home import views as home_views
from authuser import views as authuser_views
from accountuser import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_views.index, name='index'),  # URL dasar akan memanggil views.index
    path("accounts/signin/", authuser_views.custom_login_view, name="account_signin"),
    path("accounts/register/", authuser_views.custom_register_view, name="account_register"),
    path('accounts/dashboard/', authuser_views.account_dashboard, name='account_dashboard'),
    path('accounts/logout/', authuser_views.auto_logout_view, name='account_logout'),
    path('accounts/learning/', account_views.learning, name='account_learning'),
    path('news/', home_views.news, name="news"),
    path('aboutus/', home_views.aboutus, name="aboutus"),
    path('accounts/', include('allauth.urls')),
]
