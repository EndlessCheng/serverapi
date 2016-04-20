# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('payments.payments',
	url(r'$', 'payments'),
	url(r'(?P<payment_id>\w+)/$', 'payments'),
)