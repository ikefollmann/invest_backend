from django.urls import path
from . import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
]

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$')

)
