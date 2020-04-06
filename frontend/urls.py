"""bike_backend URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path
from django.urls import url

from myapp import views

urlpatterns = [
    # path('', views.Home.as_view()),
    url(r'^accident-points/?$', accidentPoint.AccidentPointList.asView(), name='accident-point-list'),
    url(r'^accident-points/(?P<pk>[0-9]+)/?$', accidentPoint.AccidentPointDetail.as_view(), name='accident-point-detail'),
    url(r'^map/P<zoom>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)/?$',
        accidentPoint.AccidentPointMap.as_view()),
        name='accident-point-map')
]
