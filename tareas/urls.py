from django.urls import path
from .views import (
    inicio,
    lista_transacciones,
    crear_transaccion,
    editar_transaccion,
    eliminar_transaccion,
    crear_contacto,
    detalle_contacto,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("dashboard/", lista_transacciones, name="dashboard"),
    path("crear/", crear_transaccion, name="crear"),
    path("editar/<int:id>/", editar_transaccion, name="editar"),
    path("eliminar/<int:id>/", eliminar_transaccion, name="eliminar"),
    path("crear-contacto/", crear_contacto, name="crear_contacto"),
    path("contacto/<int:id>/", detalle_contacto, name="detalle_contacto"),
]
