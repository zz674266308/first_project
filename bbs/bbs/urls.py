"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import os
from app01 import views
from django.views.static import serve

DIRNAME = os.path.dirname(os.path.dirname(__file__))
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': os.path.join(DIRNAME, "static/media"), 'show_indexes': True }),
    url(r'^culture/',views.Culture),
    url(r'^hello/(\d+)', views.Hello, name='hello'),
    url(r'^section(\d+)/', views.Section, name='section'),
    url(r'^login/', views.Login),
    url(r'^logout/', views.Logout),
    url(r'^register/', views.Register),
    url(r'^personal/', views.Personal),
    url(r'^data/', views.Data),
    url(r'^comments/', views.Comments),
    url(r'^delete/(\d+)', views.Delete),
    url(r'^delete_bbs/(\d+)', views.Delete_bbs),
    url(r'^publish/', views.Publish),
    url(r'^modify/', views.Modify),


]


