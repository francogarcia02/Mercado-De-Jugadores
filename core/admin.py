from django.contrib import admin
from core.models import *

class JugadorAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre',)
    fieldsets = (
        ('Datos', {'fields': ('nombre', 'club', 'posicion','edad','valor')}),
        ('Stats', {'fields': ('media','mediaritmo','mediapases','mediatiros','mediaregates','mediadefenza','mediafisico',)}),)

class DTAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre',)
    fieldsets = (
        ('Historia', {'fields': ('historia',)}),
        ('Datos', {'fields': ('nombre', 'club','valor','edad')}),)

class TrAdmin(admin.ModelAdmin):
    search_fields = ('jugador',)
    list_display = ('jugador',)
    fieldsets = (
        ('Datos', {'fields': ('jugador','customuser','created_on')}),)


"""---------------------------------------------------------------------------------"""

admin.site.register(DT, DTAdmin)
admin.site.register(Jugador,JugadorAdmin)
admin.site.register(Propios)
admin.site.register(Club)
admin.site.register(Imagen)
admin.site.register(Noticia)
admin.site.register(Transaccion, TrAdmin)

