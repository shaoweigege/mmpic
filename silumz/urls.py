"""silumz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from images import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^page/(?P<i_id>\d+)/$', views.page, name='page'),
    url(r'^page_all/(?P<i_id>\d+)/$', views.page_all, name='page_all'),
    url(r'^tag/(?P<tid>\d+)/$', views.tag, name='tag'),
    url(r'^type/(?P<typeid>\d+)/$', views.type, name='type'),
    url(r'^search/', views.search),
]
"""silumz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from images import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<i_id>\d+)/$', views.page, name='article'),
    url(r'^article_all/(?P<i_id>\d+)/$', views.page_all, name='article_all'),
    url(r'^tag/(?P<tid>\d+)/$', views.tag, name='tag'),
    url(r'^type/(?P<typeid>\d+)/$', views.type, name='type'),
    url(r'^search/', views.search),
]
