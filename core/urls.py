from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from core.views import *

urlpatterns = [
    url(r'^$',HomeView.as_view(), name='inicio'),
    url(r'^Mercado/$', Mercado.as_view(), name= "Mercado"),
    url(r'^aboutus/$', aboutus),
    url(r'^Transaccion/$', login_required(TransaCreate.as_view()), name= "Tran"),
    url(r'^TransList/$', TransList.as_view(), name= "TranL"),
    url(r'^Vender/(?P<pk>.+)$',VenderJug.as_view(), name = "Vender"),
    url(r'^Jugador_Create/$', login_required(JugadorCreate.as_view()), name= "Crear"),
    url(r'^Jugador_list/$', JugadorList.as_view(), name = "Lista"),
    url(r'^Jugador_update/(?P<pk>.+)$',login_required(JugadorUpdate.as_view()), name = "Editar"),
    url(r'^Jugador_delete/(?P<pk>.+)$',login_required(JugadorDelete.as_view()), name = "Borrar"),
    url(r'^UserCreate/$', RegistroUsuario.as_view()),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^Propios/$', login_required(Propios.as_view()), name= "MIS"),
    url(r'^Noticia_Create/$', login_required(NoticiaCreate.as_view()), name="CrearNot"),
    url(r'^Noticia_list/$', NoticiaList.as_view(), name = "notlista"),
    url(r'^Noticia_delete/(?P<pk>.+)$',login_required(NoticiaDelete.as_view()), name = "BorrarNot"),
    url(r'^Noticia_update/(?P<pk>.+)$',login_required(NoticiaUpdate.as_view()), name = "EditarNot"),




]
