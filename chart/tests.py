from django.test import TestCase as BaseTestCase

from jmbo.views import ObjectDetail
from music.models import Track
from chart.models import Chart, ChartEntry


class ChartTestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.track_public = Track.objects.create(
            title='Track public', state='published'
        )
        cls.track_public.sites = [1]
        cls.track_public.save()
        cls.track_not_public = Track.objects.create(title='Track not public')
        cls.chart = Chart.objects.create(title='Chart', state='published')
        cls.chart.sites = [1]
        cls.chart.save()
        ChartEntry.objects.create(chart=cls.chart, track=cls.track_public)
        ChartEntry.objects.create(chart=cls.chart, track=cls.track_not_public)
