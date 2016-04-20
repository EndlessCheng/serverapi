# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('orders.orders',
	url(r'^$', 'orders'),
	url(r'(?P<order_id>\w+)/$', 'orders'),
)