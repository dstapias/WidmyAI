from django.db import models
# Create your models here.

class Adenda(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return '{}'.format(self.descripcion)