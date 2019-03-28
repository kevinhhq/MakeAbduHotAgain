from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url
from database import views
from database.views import home_view, detail_view, user_create_view, delete_view, list_view, search


urlpatterns = [
    ## legacy
    path('', views.home_view, name='home'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('create/', user_create_view, name='create_view'),
    path('detail/', list_view, name='list'),
    url(r'results/$', search, name="results"),
    path('detail/<int:id>/update/', views.update_view, name='update'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete_view, name='delete_view'),
    ## end of legacy

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('database.api.urls')),
]
