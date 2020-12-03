from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from core.models import *


class JugadorForm(ModelForm):
    class Meta:
        model = Jugador

        fields = [
            'club',
            'nombre',
            'posicion',
            'edad',
            'valor',
            'mediaritmo',
            'mediapases',
            'mediatiros',
            'mediaregates',
            'mediadefenza',
            'mediafisico',

        ]

        labels = {
            'club': 'Club',
            'nombre': 'Nombre',
            'posicion': 'Posiciòn',
            'edad': 'Edad',
            'valor': 'Precio de Mercado',
            'mediaritmo': 'Estadisticas de ritmo',
            'mediapases': 'Estadistica de pases',
            'mediatiros': 'Estadistica de tiros',
            'mediaregates': 'Estadisticas de regates',
            'mediadefenza': 'Estadisticas de defenza',
            'mediafisico': 'Estadisticas del fisico',

        }

        widgets = {
            'club': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'posicion': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'mediaritmo': forms.TextInput(attrs={'class': 'form-control'}),
            'mediapases': forms.TextInput(attrs={'class': 'form-control'}),
            'mediatiros': forms.TextInput(attrs={'class': 'form-control'}),
            'mediaregates': forms.TextInput(attrs={'class': 'form-control'}),
            'mediadefenza': forms.TextInput(attrs={'class': 'form-control'}),
            'mediafisico': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UsuarioForm(UserCreationForm):
    class Meta:
        model = CustomUser

        fields = [

            'username',
            'first_name',
            'last_name',
            'email',
            'direccion'


        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo eletronico',
            'direccion': 'Direccion'

        }


class JugadorProp(ModelForm):
    class Meta:
        model = Jugador

        fields = [
            'nombre',
            'valor',

        ]

        labels = {
            'nombre': 'Nombre',
            'valor': 'Precio de Mercado',

        }


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia

        fields = [
            'epigrafe',
            'titular',
            'subtitulo',
            'entradilla',
            'cuerpo',

        ]

        labels = {
            'epigrafe': 'Epigrafe',
            'titular': 'Titulo',
            'subtitulo' : 'Subtitulo',
            'entradilla': 'Entradilla',
            'cuerpo' : 'Cuerpo',

        }

        widgets = {
            'epigrafe': forms.TextInput(attrs={'class': 'form-control'}),
            'titular': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'entradilla': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class TransaForm(ModelForm):
    class Meta:
        model = Transaccion

        fields = [
            'jugador',
            'customuser',



        ]

        labels = {
            'jugador': 'Jugador',
            'customuser': 'Su nombre',

        }





