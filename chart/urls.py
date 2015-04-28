from django.conf.urls import patterns, url

from jmbo.views import ObjectDetail


urlpatterns = patterns(
    '',
    url(
        r'^(?P<slug>[\w-]+)/$',
        ObjectDetail.as_view(),
        name='chart_object_detail'
    ),
)
