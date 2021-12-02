from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(primary_key=True,max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField()

    def __str__(self):
        return self.rut

class Profesor(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self) :
        return self.rut

class Alumno(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self) :
        return self.rut

class Cursos(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    rut = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    hora = models.CharField(max_length=20)
    fecha = models.DateField()
    sala = models.CharField(max_length=5)
    seccion = models.CharField(max_length=10)
    sigla = models.CharField(max_length=12)

    def __str__(self) :
        return self.id+' '+self.nombre

class Asistencia(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    idCurso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
    idAlumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    idProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    
    def __str__(self):
        return self.id