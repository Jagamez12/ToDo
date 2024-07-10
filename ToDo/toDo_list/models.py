from django.db import models
import datetime
# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=50)
    Terminado = models.BooleanField(default=False)
    fechaCreacion = models.DateTimeField(default=datetime.datetime.today())
    fechaFinalizacion = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=30))

class Pasos(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    terminado = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(default=1)


