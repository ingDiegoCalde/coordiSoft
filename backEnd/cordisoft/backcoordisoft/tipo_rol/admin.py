from django.contrib import admin
from tipo_rol.models import tipo_rol
@admin.register(tipo_rol)
class tipo_rolAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'slug', 'state']


