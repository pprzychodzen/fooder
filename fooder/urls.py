"""fooder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from user.views import login_request, logout_request, signup
from main.views import homepage, CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # user
    path('logout', logout_request, name="logout"),
    path('login', login_request, name='login'),
    path('register/', signup, name='register'),

    #main
    path('', CategoryListView.as_view(), name='homepage'),
    path('recipe/', CategoryListView.as_view()),
]
