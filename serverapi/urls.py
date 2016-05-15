# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from icelery.views import *
from canteens.products import *
from canteens.views import *
from canteens.canteens import *
from customers.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v1/home/$', home),
    url(r'^v1/login/$', login),
    url(r'^v1/canteens/$', canteens),
    url(r'^v1/canteens/(?P<canteen_id>\w+)/$', home),
    url(r'^v1/windows/(?P<window_id>\w+)/$', windows),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/customers/', include('customers.urls')),
    url(r'^v1/orders/', include('orders.urls')),
    url(r'^v1/payments/', include('payments.urls')),
    url(r'^v1/heatproducts/', heatgoods),
    url(r'^v1/products/(?P<product_id>\w+)/$', products),
    url(r'^v1/search/$', search),
    url(r'^v1/user/$', user_info),
                       url(r'^testcelery/', get),
                       url(r'^testsession/', test_session),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
