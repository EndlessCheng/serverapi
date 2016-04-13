from django.conf.urls import patterns, include, url


urlpatterns = patterns('users.customers',
    url(r'$', 'users'),
    url(r'(?P<customer_id>\w+)/$', 'users'),
)