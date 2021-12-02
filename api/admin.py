from django.contrib import admin
from .models import Persona,Profesor,Alumno,Asistencia,Cursos
# Register your models here.
admin.site.register(Persona)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Asistencia)
admin.site.register(Cursos)