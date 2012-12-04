from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    '',
    url(
        r'^(?P<slug>[\w-]+)/$', 
        'jmbo.views.object_detail',
        name='chart_object_detail'
    ),
)
