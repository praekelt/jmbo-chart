from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User
from django.template import RequestContext, loader

from music.models import Track
from chart.models import Chart, ChartEntry

class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com'
        )
        cls.editor.set_password("password")
        cls.editor.save()

        cls.track_public = Track.objects.create(
            title='Track public', owner=cls.editor, state='published'
        )
        cls.track_public.sites = [1]
        cls.track_public.save()
        cls.track_not_public = Track.objects.create(title='Track not public')
        cls.chart = Chart.objects.create(title='Chart', state='published')
        cls.chart.sites = [1]
        cls.chart.save()
        ChartEntry.objects.create(chart=cls.chart, track=cls.track_public, remove=False)
        ChartEntry.objects.create(chart=cls.chart, track=cls.track_not_public, remove=False)

    def test_chart_detail(self):
        response = self.client.get(self.chart.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.failUnless(
            """<table class="chart-detail-entries">""" in response.content
        )
        self.failUnless(
            "Track public" in response.content
        )
