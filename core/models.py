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
    id = models.IntegerField(primary_key=True)
    club = models.ForeignKey('Club',on_delete=models.CASCADE)
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
    club = models.ForeignKey('CLub',on_delete=models.CASCADE)
    valor= models.CharField(max_length=50,default="1")
    edad = models.CharField(max_length=50,default="1")

    class Meta:
        verbose_name = "Director Tecnico"
        verbose_name_plural = "Directores Tecnicos"
    

    def __str__(self):
        return self.nombre

"""---------------------------------------------------------------------------------"""


class Propios(models.Model):
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE)

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


class Transaccion(models.Model):
    customuser = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    jugador = models.ForeignKey('Jugador','nombre')
    created_on = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField(default = 0)
    media = models.IntegerField(default = 0)
    def save(self, *args, **kwargs):
        super(Transaccion, self).save(*args, **kwargs)
        self.precio = self.jugador.valor
        self.media = self.jugador.media
        super(Transaccion, self).save(*args, **kwargs)




class CustomUser(User):
    direccion = models.CharField('Direccion',max_length=100, default=0)

    def __str__(self):
        return self.username





