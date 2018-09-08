"""Catalogue URL Configuration

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
from django.conf.urls import *
from django.urls import path
from assignment import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^attributes/$', views.attribute_list),
    url(r'^attributes/(?P<pk>[0-9]+)$', views.attribute_detail),
    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^categories/$', views.category_list),
    url(r'^categories/(?P<pk>[0-9]+)$', views.category_detail),
]