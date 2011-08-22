from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from chart.models import Chart, ChartEntry, ChartPreferences


class ChartEntryAdmin(admin.ModelAdmin):
    list_display = ('chart', 'track', 'current_position', 'remove')
    list_filter = ('chart', 'created')
    search_fields = ('created',)

admin.site.register(Chart, ModelBaseAdmin)
admin.site.register(ChartEntry, ChartEntryAdmin)
admin.site.register(ChartPreferences)
