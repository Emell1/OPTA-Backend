from django.contrib import admin
from chatbot_app import models


@admin.register(models.TipoLead)
class TipoLeadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    ordering = ("id",)


@admin.register(models.Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo_lead")
    list_filter = ("tipo_lead",)


@admin.register(models.Momento)
class MomentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "programa")
    list_filter = ("programa",)


@admin.register(models.Submomento)
class SubmomentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "momento")
    list_filter = ("momento", "momento__programa", "momento__programa__tipo_lead")
    list_per_page = 20


@admin.register(models.Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ("submomento_str", "titulo_clean", "prioridad", "submomento")
    list_filter = ("submomento",)
    search_fields = ("titulo", "contenido")
    list_per_page = 20


@admin.register(models.Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "archivo")
    search_fields = ("nombre", "palabras_clave")
    list_per_page = 20