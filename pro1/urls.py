"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('login/',views.singIn,name="login"),
    path('postsign/',views.postsign),
    path('logout/',views.logout,name="logout"),
    path('postsignup/',views.postsignup,name='postsignup'),

    path('create/',views.create,name='upload'),
    path('post_create/',views.post_create,name='csvupload'),
    path('post_createcsv/',views.post_createcsv,name='post_createcsv'),
    path('crop/',views.crop,name='crop'),
    path('crop-video/', views.crop_video, name='crop_video'),


]
