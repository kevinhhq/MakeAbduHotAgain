"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from database import views
from database.views import home_view, detail_view, user_create_view, delete_view, list_view, search


urlpatterns = [
    path('', views.home_view, name='home'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('admin/', admin.site.urls),
    path('create/', user_create_view, name='create_view'),
    path('detail/', list_view, name='list'),
    url(r'results/$', search, name="results"),
    path('detail/<int:id>/update/', views.update_view, name='update'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete_view, name='delete_view'),
]
