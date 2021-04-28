"""upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.logincheck, name='login'),
    path('logout',views.logoutcheck,name='logout'),
    path('viewfile',views.viewfile,name='viewfile'),
    path('feed', views.feed,name='feed'),
    path('sub1', views.sub1,name='sub1'),
    path('sub2', views.sub2,name='sub2'),
    path('sub3', views.sub3,name='sub3'),
    path('sub4', views.sub4,name='sub4'),
    path('sub5', views.sub5,name='sub5'),
    path('search', views.search,name='search'),
]
