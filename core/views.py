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
    model = Jugador
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
    success_url = reverse_lazy('Mercado')


