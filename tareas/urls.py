from django.urls import path
from .views import *

urlpatterns = [
    path("", lista_transacciones, name="lista"),
    path("crear/", crear_transaccion, name="crear"),
    path("editar/<int:id>/", editar_transaccion, name="editar"),
    path("eliminar/<int:id>/", eliminar_transaccion, name="eliminar"),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
]
