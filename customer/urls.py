from django.conf.urls import patterns, include, url

from customers import *

urlpatterns = patterns('customer.customers',
    url(r'$', 'customer'),
    url(r'(?P<customer_id>\w+)/$', 'customer'),
)