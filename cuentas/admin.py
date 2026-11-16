from django.contrib import admin
from .models import Turista, Administrador, Gremio


@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    list_display = ('usuario',)


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'admin_nivel_acceso')


@admin.register(Gremio)
class GremioAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'gremio_nombre_empresa',
        'gremio_contacto'
    )