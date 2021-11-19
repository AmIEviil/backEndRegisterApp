from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import PersonaSerializer
from rest_framework import generics, views
from .models import Persona
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
        