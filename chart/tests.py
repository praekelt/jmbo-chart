from django.test import TestCase

from music.models import Track
from chart.models import Chart, ChartEntry
from chart.views import ObjectDetail

class TestCase(TestCase):

    def setUp(self):
        self.track_public = Track.objects.create(title='Track public', state='published')
        self.track_public.sites = [1]
        self.track_public.save()
        self.track_not_public = Track.objects.create(title='Track not public')
        self.chart = Chart.objects.create(title='Chart', state='published')        
        self.chart.sites = [1]
        self.chart.save()
        ChartEntry.objects.create(chart=self.chart, track=self.track_public)
        ChartEntry.objects.create(chart=self.chart, track=self.track_not_public)

    def test_object_detail(self):
        view = ObjectDetail()
        queryset = view.get_queryset(slug='chart')
        self.assertEqual(queryset.count(), 1)
