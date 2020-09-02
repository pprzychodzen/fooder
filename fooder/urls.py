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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import RecipeListView, RecipeDetail, RecipeCreateView, RecipeSearch
from user.views import login_request, logout_request, signup, UserProfileView, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # user
    path('logout', logout_request, name="logout"),
    path('login', login_request, name='login'),
    path('register/', signup, name='register'),
    path('user_profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('password/', change_password, name='change_password'),

    # main
    path('', RecipeListView.as_view(), name='homepage'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name='create_recipe'),
    path('search/', RecipeSearch.as_view(), name='search'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
