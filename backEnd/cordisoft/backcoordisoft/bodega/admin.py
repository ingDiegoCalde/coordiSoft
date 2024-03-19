from django.contrib import admin
from bodega.models import Bodega

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'slug', 'state']
