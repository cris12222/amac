from django.db import models
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel

#from users.models import AbstractFields

class MetaModelo( SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    objetivo = models.CharField(max_length=255)
    formato = models.CharField(max_length=255)
    cant_hombres = models.IntegerField()
    cant_mujeres = models.IntegerField()
    lugar = models.CharField(max_length=255)
    dirigido = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    class Meta:
        db_table = 'metas'
        ordering = ['-id']
    def __str__(self):
        return self.descripcion

class Tema( SafeDeleteModel,models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    class Meta:
        db_table = 'temas'
        ordering = ['id']
    def __str__(self):
        return self.nombre
  
class Evento( SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    apoyo = models.CharField(max_length=255)
    cant_hombres = models.IntegerField()
    cant_mujeres = models.IntegerField()
    lugar = models.CharField(max_length=255)
    dirigido = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    meta = models.ForeignKey('MetaModelo',on_delete=models.DO_NOTHING,null=True)
    descripcion = models.CharField(max_length=255)
    class Meta:
        db_table = 'eventos'
        ordering = ['-id']
    