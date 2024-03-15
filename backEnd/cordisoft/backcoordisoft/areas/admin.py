from django.contrib import admin
from areas.models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name_area', 'state']
    verbose_name_plural = 'Areas'
