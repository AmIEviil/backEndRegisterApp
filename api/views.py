from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from .serializers import AlumnoSerializer, AsistenciaSerializer, CursosSerializer, PersonaSerializer, ProfesorSerializer
from rest_framework import generics, views
from .models import Alumno, Asistencia, Cursos, Persona, Profesor
# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


class PersonasViewSet(generics.ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaBuscarViewSet(generics.ListAPIView):
    serializer_class = PersonaSerializer
    def get_queryset(self):
        elrut=self.kwargs["rut"]
        return Persona.objects.filter(rut=elrut)
    
class PersonaViewCreateSet(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
@csrf_exempt
def PersonaApi(request):
    if request.method=='GET':
        personas = Persona.objects.all()
        personas_serializar = PersonaSerializer(personas,many=True)
        return JsonResponse(personas_serializar.data,safe=False)
    if request.method=='POST':
        persona_data= JSONParser().parse(request)
        personas_serializar = PersonaSerializer(data=persona_data)
        if personas_serializar.is_valid():
            personas_serializar.save()
            return JsonResponse("Agrego Persona",safe=False)
        return JsonResponse("No pudo Agregar",safe=False)
    if request.method=='DELETE':
        try:
            persona = Persona.objects.get(rut=id)
            persona.delete()
            print("Elimino")
            return JsonResponse("Elimino",safe=False)
        except:
            return JsonResponse("No pudo Eliminar",safe=False)
    if request.method=='PUT':
        persona_data=JSONParser().parse(request)
        persona = Persona.objects.get(rut= persona_data['rut'])
        personas_serializar = PersonaSerializer(persona,data=persona_data)
        if personas_serializar.is_valid():
            return JsonResponse("Modifico",safe=False)
        return JsonResponse("No Modifico",safe=False)
#####################################################################################################################################################################
from .serializers import ProfesorSerializer

@csrf_exempt
def ProfesorAPI(request,id=0):
    if request.method=='POST':
        if id==0:
            profesores = Profesor.objects.all()
            profesor_serializar = ProfesorSerializer(profesores,many=True)
        else:
            profesores = Profesor.objects.filter(rut=id)
            profesor_serializar = ProfesorSerializer(profesores,many=True)
        return JsonResponse(profesor_serializar.data,safe=False)
    return JsonResponse("No hay Metodo",safe=False)

class ProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = ProfesorSerializer
    def get_queryset(self):
        elrut= self.kwargs["rut"]
        return Profesor.objects.filter(rut=elrut)

class CursoProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = CursosSerializer
    def get_queryset(self):
        elrut= self.kwargs["rutp"]
        return Cursos.objects.filter(rut=elrut)
#####################################################################################################################################################################
@csrf_exempt
def AlumnoAPI(request,id=0):
    if request.method=='POST':
        if id==0:
            alumno = Alumno.objects.all()
            alumno_serializar = AlumnoSerializer(alumno,many=True)
        else:
            alumno = Alumno.objects.filter(rut=id)
            alumno_serializar = AlumnoSerializer(alumno,many=True)
        return JsonResponse(alumno_serializar.data,safe=False)
    return JsonResponse("No hay Metodo",safe=False)
#####################################################################################################################################################################
@csrf_exempt
def CursosAPI(request,id=0):
    if request.method=='POST':
        cursos = Cursos.objects.all()
        curso_serializer = CursosSerializer(cursos,many=True)
        return JsonResponse(curso_serializer.data,safe=False)
    return JsonResponse("No hay Metodo",safe=False)
#####################################################################################################################################################################
@csrf_exempt
def AsistenciaAPI(request,id=0):
    if request.method=='POST':
        asistencia = Asistencia.objects.all()
        asis_serializer = AsistenciaSerializer(asistencia,many=True)
        return JsonResponse(asis_serializer.data,safe=False)
    return JsonResponse("No hay Metodo",safe=False)
@csrf_exempt
def conteo_asistencias(request):
    if request.method=='POST':        
        cantidad = Asistencia.objects.all().count()
        return JsonResponse(cantidad,safe=False)
    return JsonResponse(0,safe=False)

class AsistenciaViewSet(generics.CreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
class AsistenciaListarViewSet(generics.ListAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer