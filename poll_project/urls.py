"""poll_project URL Configuration

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

from faculty import views as faculty_views
from poll import views as poll_views
from ride import views as ride_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',poll_views.index,name='index'),
    path('create/', poll_views.create, name='create'),
    path('search/', poll_views.search, name='search'),
    path('review/', faculty_views.home, name='review'),
    # path('create/', poll_views.create,name='create'),
    path('vote/<poll_id>/', faculty_views.vote, name='vote'),
    path('results/<poll_id>/', faculty_views.results, name='results'),
    path('ride/',ride_views.journey,name='ride'),
    path('arides/', ride_views.aridess, name='aridess'),
]
