from django.conf.urls import patterns, include, url


urlpatterns = patterns('users.customers',
    # url(r'$', 'users'),
    url(r'(?P<order_id>\w+)/$', 'orders'),
)