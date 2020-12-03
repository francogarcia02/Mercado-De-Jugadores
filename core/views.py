from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from core.models import *
from .forms import *


class HomeView(TemplateView):
    template_name = 'home.html'

def aboutus(request):
    return render(request, 'Inicio/aboutus.html')

class JugadorList(ListView):
    model = Jugador
    template_name = 'Jugador/Jugador_list.html'

class JugadorCreate(CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'Jugador/Jugador_form.html'
    success_url = reverse_lazy('Lista')

class JugadorUpdate(UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'Jugador/Jugador_form.html'
    success_url = reverse_lazy('Lista')


class JugadorDelete(DeleteView):
    model = Jugador
    template_name = 'Jugador/Jugador_delete.html'
    success_url = reverse_lazy('Lista')

class Mercado(ListView):
    model = Jugador
    template_name = 'Inicio/Mercado.html'

class RegistroUsuario(CreateView):
    model = User
    template_name = 'log/UserRegister.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "log/index.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/')

class Propios(ListView):
    model = Transaccion
    template_name = 'Jugador/Propios.html'


class NoticiaList(ListView):
    model = Noticia
    template_name = 'Noticias/NotList.html'

class NoticiaCreate(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'Noticias/NotForm.html'
    success_url = reverse_lazy('notlista')

class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'Noticias/NotDelete.html'
    success_url = reverse_lazy('notlista')

class NoticiaUpdate(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'Noticias/NotForm.html'
    success_url = reverse_lazy('notlista')



class TransaCreate(CreateView):
    model = Transaccion
    form_class = TransaForm
    template_name = 'transf.html'



    def get(self, request, **kwargs):
        jugador_id = kwargs.get('jugador_id')
        if jugador_id:
            jugador = {'jugador': Jugador}
            return render(request, 'template', {"jugador": jugador})
        else:
            return render(request, 'transf.html')
    success_url = reverse_lazy('Mercado')

class TransList(ListView, ):
    model = Transaccion
    template_name = 'Transacciones/TransList.html'
"""
    queryset = Transaccion.objects.filter(customuser = CustomUser.username)

    def get(self, request, **kwargs):
        jugador_id = kwargs.get('jugador_id')
        custom = kwargs.get('username')
        customuserr = {'customuser': CustomUser}

        return render(request, 'TransList.html', {'customuser': CustomUser})

        success_url = reverse_lazy('TranL')
"""

class VenderJug(DeleteView):
    model = Transaccion
    template_name = 'Transacciones/Vender.html'
    success_url = reverse_lazy('MIS')






            #tengo que tomar el objeto y mandarlo a transf, usando request o kwargs

#context = {}
#context['jugador'] = self.request."acceder al juidador que viene del request"
#return render(request, self.template_name, context)