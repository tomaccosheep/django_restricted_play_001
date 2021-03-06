"""django_restricted_play_001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_maker import views
from django.conf import settings
#from httpproxy.views import HttpProxy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^new_project/$', views.new_project, name='new_project'),
    url(r'^index/(?P<project_id>[\w]+)/$', views.index, name='project_id'),
    url(r'^ajax/save/(?P<project_id>[\w]+)/$', views.save, name='project_id'),
    url(r'^ajax/make/(?P<project_id>[\w]+)/$', views.make, name='project_id'),
    url(r'^ajax/run/(?P<project_id>[\w]+)/$', views.run, name='project_id'),
    url(r'^view/(?P<project_id>[\w]+)/$', views.view, name='project_id'),
    url(r'^view_redirect/(?P<project_id>[\w]+)/$', views.view_redirect, name='project_id'),
    #url(r'^view/(?P<port_id>[\w]+)/$', HttpProxy.as_view(base_url=settings.PROXY_BASE_URL), name='port_id'),
    url(r'^ajax/kill/(?P<project_id>[\w]+)/$', views.kill, name='project_id'),
    
]

