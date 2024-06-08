from django.db import models
from django.utils import timezone

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fechadeposteo = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo