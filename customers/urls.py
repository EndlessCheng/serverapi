from django.conf.urls import patterns, include, url


urlpatterns = patterns('customers.customers',
    url(r'^$', 'customers'),
    url(r'(?P<customer_id>\w+)/$', 'customers'),
)