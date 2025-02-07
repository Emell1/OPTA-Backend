
from rest_framework import viewsets

from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Documento
from .serializer import (
    TipoLeadSerializer, ProgramaSerializer, MomentoSerializer,
    SubmomentoSerializer, RespuestaSerializer, DocumentoSerializer
)


class TipoLeadViewSet(viewsets.ModelViewSet):
    serializer_class = TipoLeadSerializer
    queryset = TipoLead.objects.all()


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    
    def get_queryset(self):
        
        queryset = Programa.objects.all()
        
        tipo_lead_id = self.request.GET.get('tipo_lead_id')
        if tipo_lead_id:
            return queryset.filter(tipo_lead_id=tipo_lead_id)
        return queryset


class MomentoViewSet(viewsets.ModelViewSet):
    queryset = Momento.objects.all()
    serializer_class = MomentoSerializer
    
    def get_queryset(self):
        
        queryset = Momento.objects.all()
        
        programa_id = self.request.GET.get('programa_id')
        if programa_id:
            return queryset.filter(programa_id=programa_id)
        return queryset


class SubmomentoViewSet(viewsets.ModelViewSet):
    queryset = Submomento.objects.all()
    serializer_class = SubmomentoSerializer
    
    def get_queryset(self):
        
        queryset = Submomento.objects.all()
        
        momento_id = self.request.GET.get('momento_id')
        if momento_id:
            return queryset.filter(momento_id=momento_id)
        return queryset


class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer