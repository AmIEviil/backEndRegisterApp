from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(primary_key=True,max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField()

    def __str__(self):
        return self.rut