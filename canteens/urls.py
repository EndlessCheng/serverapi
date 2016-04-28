from django.conf.urls import patterns, include, url


urlpatterns = patterns('canteens',
    # url(r'$', 'users'),
    url(r'(?P<order_id>\w+)/$', 'orders'),
                       url(r'heatgoods/$', 'products.heatgoods'),
)