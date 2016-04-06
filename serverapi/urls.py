# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin

from customer.customers import *
from customer.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^customers/', customer),
)
