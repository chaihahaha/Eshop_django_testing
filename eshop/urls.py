"""eshop URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from order.views import index  # from order.views import index
admin.autodiscover()
urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',
        serve, {"document_root": "./media", }),
    url(r'^showoff/', include('showoff.urls')),
    url(r'^accounts/', include('users.urls')),
    #    url(r'^author-polls/', include('showoff.urls',
    # namespace='author-polls')),
    #    url(r'^publisher-polls/',
    #        include('showoff.urls', namespace='publisher-polls')),
]
