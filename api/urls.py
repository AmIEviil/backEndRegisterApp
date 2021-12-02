from rest_framework import urlpatterns
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    url(r'^api/persona/$',views.PersonasViewSet.as_view()),
    url(r'^api/buscar_persona/(?P<rut>.+)/$',views.PersonaBuscarViewSet.as_view()),
    url(r'^api/persona_crear/$',views.PersonaViewCreateSet.as_view()),
    url(r'^api/persona_crear/$',views.PersonaViewCreateSet.as_view()),
    url(r'^api/persona_api/$',views.PersonaApi),
    url(r'^api/persona_apii/(?P<id>.+)/$',views.PersonaApi),
    url(r'^api/profesor/$',views.ProfesorAPI),
    url(r'^api/profe_curso/(?P<rutp>.+)$',views.CursoProfesorBuscarViewSet.as_view()),
    url(r'^api/alumno/(?P<id>.+)$',views.AlumnoAPI),
    url(r'^api/asistencia/$',views.AsistenciaViewSet.as_view()),
    url(r'^api/asistencia_l/$',views.AsistenciaListarViewSet.as_view()),
    url(r'^api/conteo/$',views.conteo_asistencias),
]

urlpatterns= format_suffix_patterns(urlpatterns)
