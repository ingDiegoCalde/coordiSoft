from django.db import models

class Tipo_rol(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    descripcion = models.TextField()
    state = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)