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
from . import views
from .views import get_queries




urlpatterns = [
    # path('', views.Home.as_view()),
    path('maps/', views.hello_maps, name='hello_maps'),
    path('login/', views.login, name='login'),
    path('queries/<int:id>/', get_queries, name='queries'),



]

"""
    path('admin/', admin.site.urls),
    path('', include('index.html')),
    path(r'^accident-points/?$', acident_point.AccidentPointList.asView(), name='accident-point-list'),
    path(r'^accident-points/(?P<pk>[0-9]+)/?$', acident_point.AccidentPointDetail.as_view(), name='accident-point'
                                                                                                  '-detail'),
    path(r'^map/P<zoom>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)/?$',
         acident_point.AccidentPointMap.as_view(),
         name='accident-point-map')
"""
