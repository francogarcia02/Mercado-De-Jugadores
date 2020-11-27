from django.db import models
from django.db import transaction
from django.contrib.auth.models import User


"""---------------------------------------------------------------------------------"""

class Club(models.Model):
    club = models.CharField(max_length=50)
    historia = models.CharField(max_length=50)
    titulos = models.CharField(max_length=50)

    def __str__(self):
        return self.club

"""---------------------------------------------------------------------------------"""


class Jugador(models.Model):
    posiciones= [
        ('Delantero', 'Delantero'),
        ('Mediocampo', 'Mediocampo'),
        ('Defenzor', 'Defenzor'),
        ('Arquero', 'Arquero'),
    ]
    club = models.ForeignKey('Club','on_delete',max_length=50)
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50,choices=posiciones,blank=True,)
    edad = models.IntegerField(default= 0)
    valor= models.IntegerField(default=0)
    media = models.IntegerField(default=0)
    mediaritmo = models.IntegerField(default=0)
    mediapases= models.IntegerField(default=0)
    mediatiros = models.IntegerField(default=0)
    mediaregates = models.IntegerField(default=0)
    mediadefenza = models.IntegerField(default=0)
    mediafisico = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return self.nombre


"""---------------------------------------------------------------------------------"""


class DT(models.Model):

    historia = models.CharField(max_length=60, default='NULL')
    nombre = models.CharField(max_length=50)
    club = models.ForeignKey('CLub','on_delete',max_length=50)
    valor= models.CharField(max_length=50,default="1")
    edad = models.CharField(max_length=50,default="1")

    class Meta:
        verbose_name = "Director Tecnico"
        verbose_name_plural = "Directores Tecnicos"
    

    def __str__(self):
        return self.nombre

"""---------------------------------------------------------------------------------"""

class Usuario(models.Model):
    dinero = models.IntegerField(default=1000)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "Usuarios"

class Propios(models.Model):
    jugador = models.ForeignKey('Jugador', 'on_delete', max_length=50,default=1)

    class Meta:
        verbose_name = "Propio"
        verbose_name_plural = "propios"

class Imagen(models.Model):
    pass
class Noticia(models.Model):
    epigrafe = models.CharField(max_length=100)
    titular = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length= 100)
    entradilla = models.CharField(max_length=300)
    cuerpo = models.CharField(max_length = 2000)


class Transaccion(Jugador):
    fecha = models.DateTimeField(auto_now_add=True)





