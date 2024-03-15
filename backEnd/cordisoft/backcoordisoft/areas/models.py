from django.db import models

class Area(models.Model):
    name_area = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) #solo van a poder crear un area con el mismo nombre
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.name_area