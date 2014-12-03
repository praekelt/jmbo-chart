from django.conf.urls.defaults import patterns, include


urlpatterns = patterns(
    '',
    (r'^jmbo/', include('jmbo.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^music/', include('music.urls')),
    (r'^chart/', include('chart.urls')),
)
