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
]

urlpatterns= format_suffix_patterns(urlpatterns)
