from django.db.models import fields
from .models import Persona,Profesor,Alumno,Asistencia,Cursos
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ["rut","nombre","apellido","edad"]

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["rut","nombre","apellido","password"]

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["rut","nombre","apellido","password"]

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","idCurso","idAlumno","idProfesor","fecha","hora"]

        
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ["id","rut","nombre","hora","fecha","sala","seccion","sigla"]
