from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from preferences.models import Preferences
from jmbo.models import ModelBase
from music.models import Track


class Chart(ModelBase):

    @property
    def chartentries_permitted(self):
        return self.chartentries.filter(
            track__in=Track.permitted.all()
        ).order_by('current_position')


class ChartEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    chart = models.ForeignKey(
        Chart,
        related_name='chartentries'
    )
    track = models.ForeignKey(Track)
    previous_position = models.IntegerField(
        blank=True,
        null=True
    )
    current_position = models.IntegerField(
        blank=True,
        null=True
    )
    next_position = models.IntegerField(
        blank=True,
        null=True
    )
    remove = models.BooleanField(
        help_text="On the next update this entry will be removed completely."
    )

    class Meta:
        verbose_name = 'Chart entry'
        verbose_name_plural = 'Chart entries'
        ordering = ['current_position']

    def get_duration_on_chart(self):
        now = timezone.now()
        if not timezone.is_aware(self.created):
            now = datetime.now()
        return now - (now - self.created)

    def __unicode__(self):
        return '%s Entry %s' % (self.chart.title, self.current_position)


class ChartPreferences(Preferences):
    __module__ = 'preferences.models'

    primary_chart = models.ForeignKey(
        'chart.Chart',
        null=True,
        help_text="Select the primary chart link from the navigation.",
        related_name='chartoptions_primary_chart',
        limit_choices_to={'state': 'published'}
    )

    class Meta:
        verbose_name = 'Chart preferences'
        verbose_name_plural = 'Chart preferences'
