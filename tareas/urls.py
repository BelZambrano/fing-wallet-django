from django.urls import path
from .views import (
    lista_transacciones,
    crear_transaccion,
    editar_transaccion,
    eliminar_transaccion,
    crear_usuario,
)

urlpatterns = [
    path("", lista_transacciones, name="lista"),
    path("crear/", crear_transaccion),
    path("editar/<int:id>/", editar_transaccion),
    path("eliminar/<int:id>/", eliminar_transaccion),
    path("crear-usuario/", crear_usuario),
]
