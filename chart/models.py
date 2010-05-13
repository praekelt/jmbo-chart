from django.core.urlresolvers import reverse
from django.db import models

from content.models import ModelBase


class Chart(ModelBase):
    class Meta:
        verbose_name = 'Chart'
        verbose_name_plural = 'Charts'
    
    def get_absolute_url(self):
        return reverse('chart_object_detail', kwargs={'slug': self.slug})
        
    def __unicode__(self):
        return self.title

class ChartEntry(ModelBase):
    chart = models.ForeignKey(
        Chart, 
        related_name='chartentries'
    )
    # TODO: add radio.models.Song foreign key to model
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
        verbose_name = 'Chart Entry'
        verbose_name_plural = 'Chart Entries'
        ordering = ['current_position']
    
    def position_difference(self):
        return str(self.current_position - self.position_difference)
    
    def __unicode__(self):
        return '%s entry %s' % (self.chart.title, self.current_position)
