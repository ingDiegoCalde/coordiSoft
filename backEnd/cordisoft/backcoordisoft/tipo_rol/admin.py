from django.contrib import admin
from tipo_rol.models import Tipo_rol
@admin.register(Tipo_rol)
class tipo_rolAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'slug', 'state']


