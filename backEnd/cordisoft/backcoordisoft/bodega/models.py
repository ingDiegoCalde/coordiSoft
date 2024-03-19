from django.db import models
from django.db.models import SET_NULL
from users.models import User
from areas.models import Area

class Bodega(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    descripcion = models.TextField()
    state = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    encargado = models.ForeignKey(User, on_delete=SET_NULL, null=True)


