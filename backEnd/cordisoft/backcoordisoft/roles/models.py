from django.db import models
from django.db.models import SET_NULL
from users.models import User
from tipo_rol.models import Tipo_rol

class Bodega(models.Model):
    persona = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    tiporol = models.ForeignKey(Tipo_rol, on_delete=SET_NULL, null=True)

    slug = models.SlugField(max_length=255, unique=True)
    descripcion = models.TextField()
    state = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    encargado = models.ForeignKey(User, on_delete=SET_NULL, null=True)


